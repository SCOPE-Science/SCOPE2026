# Exact joint-enumerator obstruction for binary \([20,8,7]\) LCD codes

## Finding
Every binary linear complementary-dual (LCD) code \(C\subseteq\mathbb F_2^{20}\) of dimension \(8\) has minimum Hamming distance \(d(C)\leq6\). More precisely, the real joint-weight-enumerator feasibility relaxation at \((n,k,d)=(20,8,7)\) is empty. The attached rational Farkas certificate is checked exactly, without a floating-point sign decision.

## Assumptions and scope
An LCD code means \(C\cap C^\perp=\{0\}\) for the standard binary dot product. We use only length \(20\), dimension \(8\), and the contrary hypothesis \(d(C)\ge7\). Nothing asserts the existence of an LCD code achieving distance \(6\); the result is an upper bound and an exact infeasibility certificate for the specified relaxation, not a classification of codes.

For \((u,v)\in C\times C^\perp\) define the pattern \((a,b,c,e)\) by counting coordinates \((0,0),(0,1),(1,0),(1,1)\), respectively. Write \(M_{a,b,c,e}\ge0\) for the number of such ordered pairs, where \(a+b+c+e=20\). There are \(\binom{23}{3}=1771\) possible pattern types. Orthogonality requires \(e\) even; distance \(\ge7\) eliminates \(1\le c+e\le6\); and the LCD condition eliminates \(b=c=0\), \(e>0\). Exactly \(686\) pattern types survive these three mandatory zero conditions.

## Proof
For \(0\le w\le20\), abbreviate \(A_w=M_{20-w,0,w,0}\), \(B_w=M_{20-w,w,0,0}\). Since \(|C|=2^8\), \(|C^\perp|=2^{12}\), and \(C\oplus C^\perp=\mathbb F_2^{20}\), every actual joint enumerator satisfies
\[
\sum_{c+e=w}M_{a,b,c,e}=2^{12}A_w,\qquad
\sum_{b+e=w}M_{a,b,c,e}=2^8B_w,\qquad
\sum_{b+c=w}M_{a,b,c,e}=\binom{20}{w}.
\]
Also \(M_{20,0,0,0}=1\). Binary MacWilliams duality supplies, for \(0\le j\le20\),
\[
2^8 B_j=\sum_{w=0}^{20}K_j(w)A_w,\quad
K_j(w)=\sum_{t=0}^j(-1)^t\binom wt\binom{20-w}{j-t}.
\]
These identities are indexed in `verify.py` as 85 equations: for each \(w\), the code marginal, dual marginal, then ambient marginal, followed by the normalization equation and the 21 MacWilliams equations.

The joint MacWilliams identity uses the integer matrix
\[
H=\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}
\]
and says \(J(x)=2^{-20}J(Hx)\), where \(J(x)=\sum M_{a,b,c,e}x_0^a x_1^b x_2^c x_3^e\). For each target pattern \(\beta\), its coefficient identity has the form \(\sum_\alpha (T_{\alpha\beta}-2^{20}\delta_{\alpha\beta})M_\alpha=0\), where \(T_{\alpha\beta}\) is the integer coefficient of the target monomial in \(\prod_{r=0}^3(\sum_{s=0}^3H_{rs}x_s)^{\alpha_r}\). The verifier reconstructs all these integers using degree-by-degree polynomial multiplication.

`CERTIFICATE.json` gives signed rational multipliers for 74 of the 85 first equations and 427 of the joint identities: each listed numerator \(t\) is multiplied by \(1/10^{12}\), and a joint term with stored auxiliary denominator \(p\) is multiplied by \(1/(10^{12}p)\). Add \(1/10000\) times the sum of all 21 ambient equations divided by \(2^{20}\). This adds \(1/10000\) to every joint coefficient, and \(1/10000\) to the right-hand side.

The checker confirms by exact integer and rational arithmetic that the resulting right-hand side is
\[
-\frac{999899898449}{10^{12}}<0,
\]
while every one of the \(686\) allowed nonnegative \(M_\alpha\) has **strictly positive** coefficient. The left-hand side of this valid linear combination must therefore be nonnegative, contradicting its negative right-hand side. No integrality, existence-oracle, or numerical solver assumption is needed to validate the certificate. Consequently no binary LCD \([20,8,d]\) code exists for \(d\ge7\).

## Verification
The self-contained `verify.py` (Python 3 standard library only) reads `CERTIFICATE.json` next to itself. Execute `python3 verify.py`. It rebuilds the 1771 degree-20 monomials, the exact 1771-row Hadamard coefficient transform, the 85 marginal/ordinary duality constraints, and the 686 admissible nonnegative variables; it then computes the certificate's combined coefficients and right-hand side as exact fractions. A successful run ends with `VERIFY_OK`. The constraints are rederived from the mathematical definitions in this note, not taken from a solver log.

## Relationship to prior work
Alahmadi–Deza–Dutour Sikirić–Solé introduced the joint-weight-enumerator LP and proved its invariant-theoretic basis. Their tabulated computations cover lengths through 16, not this parameter point. Kang–Xiong's September 2026 paper supplies its precise Appendix A benchmark and reports \(D_{\mathrm M}(20,8)=6\) against an exactly justified Gauss-phase endpoint \(D_{\mathrm G}(20,8)=7\), but explicitly marks the joint value as **screening**, not exact verification. The present exact rational infeasibility certificate verifies the missing exclusion at distance 7. It does not reassert the original numerical estimate as a new discovery, nor provide a rational feasible point at distance 6. Thus it proves \(D_{\mathrm M}(20,8)\le6\), and hence strict separation from the reported exact Gauss-phase endpoint 7. Searches for equivalent certificates and bounds found no prior published exact certificate for this case; that negative search is not a global novelty guarantee.

## Limitations
This is the particular binary length/dimension instance \((20,8)\). The obstruction does not imply the existence of an LCD \([20,8,6]\) code and does not address generalized weights, other parameters, or an intrinsic dominance relation between the two LP constructions. The certificate verifies a relaxation's infeasibility; it does not classify all LCD codes.

## References
1. Kang and Xiong, *Linear programming bounds for binary and ternary LCD Codes*, arXiv:2609.08662v2 (first public 2026-09-08), Section 5.3, Table 4, Appendix A. https://arxiv.org/html/2609.08662v2
2. Alahmadi, Deza, Dutour Sikirić, and Solé, *The joint weight enumerator of an LCD code and its dual*, arXiv:1511.08889v1 (2015), Propositions III.1–III.2 and Section IV. https://arxiv.org/html/1511.08889v1
