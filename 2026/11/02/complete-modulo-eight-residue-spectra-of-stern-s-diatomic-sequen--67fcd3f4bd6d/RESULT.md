# Complete modulo-eight residue spectra of Stern’s diatomic sequence on dyadic blocks

## Finding

Let \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\). For every integer \(r\geq0\) and residue \(j\in\{0,1,\ldots,7\}\), set
\[
C_{r,j}=\#\{0\leq n<2^r:s(n)\equiv j\pmod8\},\qquad G_j(t)=\sum_{r\geq0}C_{r,j}t^r.
\]
The following **eight exact rational generating functions** hold simultaneously. Define four denominators:
\[
\begin{aligned}
D_0(t)&=(1-t)(1+t)(1-2t)(1-t+2t^2)(1-t^2+4t^4),\\
D_o(t)&=(1-t)(1+t)(1-2t)(1+t^2)(1-2t+3t^2-4t^3+4t^4),\\
D_2(t)&=(1-t)^2(1+t)(1-2t)(1-t+2t^2),\\
D_4(t)&=(1+t)(1-2t)(1-t+2t^2)(1-t^2+4t^4).
\end{aligned}
\]
For all eight residues, \(G_j(t)=P_j(t)/D_{\kappa(j)}(t)\), with \(\kappa(0)=0\), \(\kappa(2)=\kappa(6)=2\), \(\kappa(4)=4\), and \(\kappa(j)=o\) for odd \(j\). The numerator table is
\[
\begin{array}{c|l}
j&P_j(t)\\\hline
0&1-2t+2t^3-t^4-6t^5+6t^6-8t^8\\
1&t-2t^2+2t^3-4t^4+t^5+6t^6-8t^7+12t^8-16t^9\\
2&t^2-2t^3+t^4-2t^6\\
3&2t^3-4t^4+4t^5-4t^6+2t^7+4t^8-8t^9\\
4&2t^4\\
5&2t^4-2t^5+2t^6-2t^7-4t^8+8t^9\\
6&2t^6\\
7&4t^5-8t^6+12t^7-12t^8+16t^9
\end{array}
\]
Each fraction is reduced in \(\mathbb Q(t)\). In addition, for every residue \(j\),
\[
C_{r,j}=\rho_j2^r+O(2^{r/2}),\qquad
\rho_j=\begin{cases}1/12,&j\text{ even},\\1/6,&j\text{ odd},\end{cases}
\]
and **the exponent \(1/2\) is best possible for every one of the eight residues**:
\[
\limsup_{r\to\infty}\frac{|C_{r,j}-\rho_j2^r|}{2^{r/2}}>0
\qquad (j=0,\ldots,7).
\]

## Assumptions and scope

There is no field restriction or asymptotic size hypothesis. The recurrence and all formulas hold for the ordinary integer Stern sequence, every integer dyadic depth \(r\geq0\), and every residue modulo eight. The asymptotic assertion concerns only dyadic endpoints \(2^r\), not arbitrary interval endpoints.

## Proof

**Transfer states.** The pairs \((s(n),s(n+1))\) are primitive modulo eight. Consequently they belong to the \(48\)-element set
\[\mathcal S=\{(a,b)\in(\mathbb Z/8\mathbb Z)^2:\text{at least one of }a,b\text{ is odd}\}.\]
The two descendants of a pair are \(L(a,b)=(a,a+b)\) and \(R(a,b)=(a+b,b)\), with coordinates reduced modulo eight. These follow directly by taking the Stern relations at indices \(2n\) and \(2n+1\). Let \(A\) be the \(48\times48\) integer adjacency matrix with one edge per descendant (parallel edges counted), let \(e\) be the indicator of \((0,1)\), and let \(w_j\) indicate states whose first coordinate is \(j\). Iterating binary digits (including leading zeros, which fix the initial state) proves
\[C_{r,j}=w_j^{\mathsf T}A^r e.\]

**Exact finite annihilators.** Write \(Q_j(t)=D_{\kappa(j)}(t)\) and \(d_j=\deg Q_j\), and define \(H_j(X)=X^{d_j}Q_j(X^{-1})\). Exhausting all \(48\) possible states by the explicitly specified maps gives the exact integer row-vector identities
\[
\begin{aligned}
w_j^{\mathsf T}H_j(A)&=0 &&(j=0),\\
w_j^{\mathsf T}A H_j(A)&=0 &&(j=1,2,3,5,6,7),\\
w_4^{\mathsf T}H_0(A)&=0.&&
\end{aligned}
\]
The accompanying standalone verifier reconstructs these rows using only integer additions and checks every coordinate equals zero; there are no floating-point operations, truncated searches, or guessed eigenvalues. The first \(d_j+1\) scalar values obtained from the same transfer construction yield \(P_j(t)\) above by coefficient comparison of \(Q_j(t)G_j(t)\). In the case \(j=4\), the first nine values together with the verified annihilator \(H_0(A)\) establish the shorter fraction because \(D_0(t)=(1-t)D_4(t)\): the proposed shorter recurrence implies the longer one, and nine initial terms uniquely determine any solution of the longer recurrence. This proves the eight rational identities for every \(r\), not merely through a tested cutoff. Euclidean polynomial division confirms that each numerator is coprime to its denominator (also checked with exact rational arithmetic in the verifier).

**Densities and upper bounds.** Both \(L\) and \(R\) are invertible permutations of \(\mathcal S\), so each vertex has exactly two outgoing and two incoming edges. These two elementary transformations generate a transitive action on primitive vectors modulo eight: because at least one coordinate is a unit, elementary additions and their powers reduce any vector to \((0,1)\). The state graph is strongly connected and has a self-loop at \((0,1)\), hence is aperiodic. Therefore \(A/2\) has uniform stationary distribution, and \(C_{r,j}/2^r\) approaches the fraction of states with first coordinate \(j\): four of \(48\) for even \(j\), eight of \(48\) for odd \(j\). In the displayed denominators every root of the reciprocal characteristic factors other than \(2\) has modulus at most \(\sqrt2\), with a possible repeated root \(1\) for even residues. More precisely, the factors \(X^2-X+2\), \(X^4-X^2+4\), and \(X^4-2X^3+3X^2-4X+4\) have all roots on \(|X|=\sqrt2\). For the last two quartics, putting \(X=\sqrt2 z\), dividing by \(z^2\), and setting \(u=z+z^{-1}\) gives respectively \(u^2=5/2\) and \(u^2-\sqrt2 u-1/2=0\); their real solutions all lie in \((-2,2)\), so \(|z|=1\). The remaining roots are \(0\), \(1\), \(-1\), or \(\pm i\). Partial fractions prove the displayed \(O(2^{r/2})\) bounds (the possible linear-in-\(r\) term from the repeated root \(1\) is smaller).

**Sharpness for every class.** All eight fractions are reduced, and each denominator has at least one of the just-listed factors whose roots have modulus \(\sqrt2\). Consequently the partial-fraction expansion contains at least one nonzero mode of magnitude \(2^{r/2}\) for each residue. The collection of these modes has distinct frequencies. Its squared modulus has strictly positive Cesàro mean after division by \(2^r\), by orthogonality of distinct unit-circle exponentials. The lower-modulus modes disappear in this normalization, so the asserted positive limsup follows separately for every residue.

## Verification

Run `python3 verify_stern8.py` from the directory containing the accompanying file. It (i) enumerates all \(48\) legitimate states and checks the exact annihilator identities componentwise, (ii) verifies irreducibility and aperiodicity of the directed state graph by exact reachability, (iii) checks the eight generating-function identities against computed transfer counts, (iv) independently enumerates all \(2^r\) Stern values for \(0\leq r\leq17\), and (v) uses exact rational Euclidean division to prove coprimality of every numerator and denominator. A successful replay prints `VERIFY_OK states=48 residues=8 row_certificates=8 direct_levels=18 last_depth=17`. The finite row identities plus the recurrence argument, rather than the direct finite enumerations, provide the all-depth certificate.

## Relationship to prior work

Reznick, *Regularity properties of the Stern enumeration of the rationals* (public preprint October 19, 2006; Journal of Integer Sequences, 2008), proves uniform distribution of primitive Stern residue pairs for general moduli and gives exact dyadic formulas specifically for the smaller moduli two and three. His work supplies the foundational pair dynamics and the leading densities here, but not the eight simultaneous exact generating functions or the eight individually sharp square-root errors. It also notes that the divisibility counts at moduli eight and six need not coincide. Prior related results on the exact difference of these two divisibility counts do not determine the other seven classes, and their difference law is not claimed here. Lansing's dissertation (2014) examines related Stern-derived sequences and different parity/digital-statistic questions; Defant (2016) studies upper bounds for Stern values rather than modulo-eight residue histograms. The integer-transfer approach itself is standard; the new content is the explicit, complete, reduced eight-fraction evaluation and the classwise optimal exponent.

## Limitations

No claim is made for fixed non-dyadic endpoints, other moduli, or finer joint distributions of adjacent Stern values. Novelty comparisons included accessible primary sources and earlier exact modulus-eight versus modulus-six results, but unlocated treatments of this specific special case could exist. Independent mathematical review has not been performed.

## References

1. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601 (first publicly posted October 19, 2006), and *Journal of Integer Sequences* 11 (2008), Article 08.4.1, https://arxiv.org/abs/math/0610601 ; https://cs.uwaterloo.ca/journals/JIS/VOL11/Reznick/reznick4.pdf .
2. J. Lansing, *On the Stern sequence and a related sequence*, 2014 dissertation, https://oeis.org/A240388/a240388.pdf .
3. C. Defant, *Upper Bounds for Stern's Diatomic Sequence and Related Sequences*, *Electronic Journal of Combinatorics* 23 (2016), Article P4.8, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i4p8 .
