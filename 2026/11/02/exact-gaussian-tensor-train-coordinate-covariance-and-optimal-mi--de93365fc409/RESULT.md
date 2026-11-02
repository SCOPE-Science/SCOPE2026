# Exact Gaussian tensor-train coordinate covariance and optimal mismatch spacing

## Finding

The squared-coordinate covariance kernel of a real, isotropically normalized Gaussian tensor-train (TT) vector has an exact three-state transfer representation. At every finite bond rank the covariance is explicit; for bond rank greater than one, it depends not merely on the number of differing physical indices but on the *gaps between their locations*. This gives an exact, sharp arrangement theorem and an exact variance formula for TT Girard–Hutchinson estimators of diagonal matrices.

Let \(d\ge2\) and \(n\ge2\) be integers and let \(r\ge1\) be the common TT bond rank. Set
\[
 c=1+\frac2r,\qquad z=\frac{r-1}{r+2},\qquad F(g)=\frac{1+2z^g}{3}\quad(g\in\{1,2,\dots\}).
\]
For distinct physical multi-indices \(I,J\in\{1,\dots,n\}^d\), write \(j_1<\dots<j_k\) for exactly those positions at which they differ. Then
\[
 \boxed{\mathbb E[\omega_I^2\omega_J^2]=c^{d-1}\prod_{s=1}^{k-1} F(j_{s+1}-j_s).}
\]
An empty product is one. On the diagonal, \(\mathbb E[\omega_I^4]=3c^{d-1}\), and \(\mathbb E[\omega_I^2]=1\). Thus the covariance is the displayed mixed fourth moment minus one and is nonnegative; for distinct indices it vanishes exactly if they differ at all \(d\) positions.

For \(r>1\) and \(2\le k\le d\), among all possible placements of exactly \(k\) mismatching positions, the largest mixed fourth moment is
\[
 \boxed{K_{\max}=c^{d-k},}
\]
attained precisely when the mismatches form one consecutive block (the condition is automatic when \(k=d\)). The smallest is attained precisely when the first and last modes differ and the \(k-1\) consecutive gaps between mismatches are as equal as possible. Explicitly, with \(q=\lfloor(d-1)/(k-1)\rfloor\), \(t=(d-1)-(k-1)q\),
\[
 \boxed{K_{\min}=c^{d-1}F(q)^{k-1-t}F(q+1)^t.}
\]
When \(k=1\), placement does not matter. When \(r=1\), every configuration with \(k\ge1\) has mixed moment \(3^{d-k}\), so the spacing effect is genuinely a positive-bond-rank phenomenon.

For arbitrary real diagonal \(A=\operatorname{diag}(a_I)\), the average of \(m\ge1\) independent TT quadratic-form samples has exact variance
\[
 \boxed{\operatorname{Var} H_m(A)=\frac1m\sum_{I,J}a_Ia_J\bigl(K(I,J)-1\bigr),}
\]
where \(K(I,J)\) is the corresponding mixed fourth moment above. For a nonnegative two-spike diagonal, endpoint-spanning placements with balanced gaps minimize this variance among all permutations with the same mismatch count; there may be several equally optimal orders of the balanced gaps.

## Assumptions and scope

All TT core entries are mutually independent real \(N(0,1)\) random variables. With bond indices \(b_1,\ldots,b_{d-1}\in\{1,\dots,r\}\), define the coordinate
\[
 \omega_I=r^{-(d-1)/2}\sum_{b_1,\dots,b_{d-1}=1}^r
 G^{[1]}_{i_1,b_1}G^{[2]}_{b_1,i_2,b_2}\cdots G^{[d]}_{b_{d-1},i_d}.
\]
The independent cores have the indicated endpoint shapes and interior shape \(r\times n\times r\). This is exactly the real Gaussian TT normalization of Definition 1 in Bujanović–Kressner–Olić. The estimator is \(H_m(A)=m^{-1}\sum_{h=1}^m\omega_h^{\mathsf T} A\omega_h\), using independent copies \(\omega_h\). The coordinate calculation does not assume that \(A\) is positive semidefinite, although the interpretation of optimal two-spike placement uses nonnegative diagonal entries.

## Proof

**Second moment.** The independence of cores and the Gaussian second-moment identity force each bond in a pair of copies to coincide; the normalization cancels exactly. Thus \(\mathbb E[\omega_I\omega_J]\) is one for \(I=J\) and zero otherwise.

**Four-replica Wick transfer.** Expand \(\omega_I^2\omega_J^2\) as a sum over four independently indexed bond paths, but reuse the same random Gaussian cores. At each mode Isserlis' identity gives the three Wick pairings of the four replica indices,
\[
 \pi_0=(12)(34),\quad\pi_1=(13)(24),\quad\pi_2=(14)(23).
\]
At a physical position where \(I\) and \(J\) differ, independence of the Gaussian variables permits only \(\pi_0\); at a shared physical position, all three pairings are permitted. At a bond joining neighboring modes, equal pairings identify the four bond replicas into two classes and contribute \(r^2\) free assignments. Distinct pairings identify all four into one class and contribute \(r\). After multiplication by the normalization \(r^{-2(d-1)}\), a sequence \((\pi_1,\ldots,\pi_d)\) therefore has transfer weight
\[
 \prod_{j=1}^{d-1}T_{\pi_j,\pi_{j+1}},\qquad
 T_{uv}=\begin{cases}1,&u=v,\\1/r,&u\ne v.\end{cases}
\]
Summing over pairings compatible with the physical indices proves the exact three-state transfer representation. (The \(\pi_j\) in this paragraph label Wick states, not the mismatch locations.)

The symmetric \(3\times3\) matrix \(T\) has constant-vector eigenvalue \(c=1+2/r\) and two orthogonal eigenvalues \(a=1-1/r\). Hence
\[
 (T^g)_{00}=\frac{c^g+2a^g}{3}=c^g F(g).
\]
If there is no mismatch, all states are allowed and the sum is \(\mathbf1^{\mathsf T}T^{d-1}\mathbf1=3c^{d-1}\). Otherwise the mismatch sites pin the Wick state to \(\pi_0\), the free exterior segments each supply their Perron factor, and the gaps supply \((T^g)_{00}\). This is exactly the claimed product formula, including mismatches at endpoints.

**Covariance and strict positivity.** The all-\(\pi_0\) transfer path has weight one. Every remaining permitted Wick path has nonnegative weight. If some mode is shared, changing the pairing only at that mode gives an additional positive-weight path, and if every mode differs only the all-\(\pi_0\) path is allowed. Thus distinct-coordinate covariance is positive exactly when some physical mode agrees. Combining with the already proved second moment gives the covariance formula.

**Sharp arrangement.** For \(r>1\), the ratio \(z=a/c\) lies strictly between zero and one. The function \(F(g)=(1+2z^g)/3\) is strictly decreasing in positive integer \(g\). Therefore maximizing the product requires making each gap equal to one. Also
\[
 \frac{\mathrm d^2}{\mathrm dx^2}\log F(x)
 =\frac{2z^x(\log z)^2}{(1+2z^x)^2}>0\quad(x>0).
\]
Minimization first uses the full available span \(d-1\), because increasing a gap strictly decreases the product. For this fixed sum, strict convexity and elementary pairwise averaging show that the integer gaps differ by at most one; the endpoint and gap conditions are thus necessary and sufficient. Substituting the balanced gaps gives \(K_{\min}\). Since \(F(1)=1/c\), consecutive mismatches give \(K_{\max}=c^{d-k}\). For \(r=1\), the factor \(z=0\) makes \(F(g)=1/3\) for every positive integer gap, giving the stated degeneracy.

**Trace-estimator variance.** Diagonality gives \(\omega^{\mathsf T}A\omega=\sum_I a_I\omega_I^2\). Expanding its variance and averaging independent copies proves the finite double-sum identity without requiring \(a_I\ge0\). For two equal nonnegative spikes at indices \(I,J\), the variance becomes \(m^{-1}[2(3c^{d-1}-1)+2(K(I,J)-1)]\), so the arrangement theorem transfers immediately to the variance.

**Exact witness.** Take \(d=4\), \(n=2\), \(r=2\), and one sample. Put equal diagonal entries \(a_I=a_J=1\) and all other entries zero. Fix \(I=(1,1,1,1)\). For \(J=(2,2,1,1)\), two mismatches are adjacent: \(K=4\), giving \(\operatorname{Var}H_1=52\). For \(J=(2,1,1,2)\), mismatches occupy the endpoints: \(K=11/4\), giving \(\operatorname{Var}H_1=99/2\). Both matrices have exactly two unit eigenvalues and trace two.

## Verification

The accompanying standard-library \(\texttt{CHECK.py}\) evaluates the exact formula against independent Wick expansion over every four-replica bond path in all binary mismatch patterns for \((d,r)=(2,2),(3,2),(3,3),(4,2)\). It separately checks the rational three-state transfer recurrence, all configurations through order nine at bond ranks one through seven, and the exact upper and lower arrangement bounds through order eleven at bond ranks one through eight. The delivered checker reports \(\texttt{CHECKS\_PASSED 22694}\). These finite checks are not used as proof of statements quantified over every order and bond rank; those follow from the transfer-matrix and convexity arguments above.

## Relationship to prior work

Bujanović, Kressner and Olić (2026), Definition 1 and Theorem 5, establish this Gaussian TT construction, isotropy, and a sharp individual coordinate fourth moment as a special case of their rank-one-tensor contraction moment equality; they derive trace-estimation concentration bounds rather than the multi-mismatch covariance kernel or sharp mode-spacing classification. The \(I=J\) formula is thus not claimed as a new observation. Their paper was first public on June 14, 2026.

Meyer and Avron (2023), Theorem 1, give an exact variance formula for Kronecker products of Gaussian vectors, which corresponds to the bond-rank-one specialization; that specialization is already within their broader result and is included only as a consistency check. Rakhshan and Rabusseau (2020), Theorem 1, analyze random TT projections via moment and variance bounds without the positionwise cross kernel. Cazeaux, Dupuy and Justiniano (2026), Proposition 7.4, give a partial-trace second-moment upper bound for real Gaussian TTStack sketches rather than this exact coordinatewise law. The positive-bond-rank mixed covariance and its sharp permutation extremizers are the subject of the present finding.

## Limitations

The result assumes independent real Gaussian cores, a fixed finite integer bond rank, a single TT-vector distribution and diagonal matrices for the trace-estimator formula. For a general nondiagonal matrix the displayed diagonal variance formula does not apply. The arrangement comparison fixes the number of mismatching sites and the weights of a nonnegative two-spike diagonal; it does not give a universal optimum permutation for arbitrary diagonal data. No general concentration or full tensor-train algorithm complexity bound is asserted. The use of Wick transfer matrices is classical; a historically earlier mathematically equivalent finite-rank coordinate-kernel identity remains a priority risk despite the inspected comparisons.

## References

- Z. Bujanović, D. Kressner and H. Olić, *Stochastic trace estimation with tensor train random vectors*, arXiv:2606.15679, first posted 2026-06-14, https://arxiv.org/abs/2606.15679 (Definition 1; Lemma 2; Theorem 5; Theorem 7).
- R. A. Meyer and H. Avron, *Hutchinson's Estimator is Bad at Kronecker-Trace-Estimation*, arXiv:2309.04952, first posted 2023-09-10, https://arxiv.org/abs/2309.04952 (Theorems 1 and 2).
- B. Rakhshan and G. Rabusseau, *Tensorized Random Projections*, arXiv:2003.05101, 2020, https://arxiv.org/abs/2003.05101 (Theorem 1 and proof).
- A. Cazeaux, V. Dupuy and P. Justiniano, *Linear-Scaling Tensor Train Sketching*, arXiv:2603.11009, 2026, https://arxiv.org/abs/2603.11009 (Proposition 7.4).
