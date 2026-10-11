# A sign obstruction to the tensor-product characterization of controlled \(g\)-fusion frames

## Finding
Theorem 4 of Ghosh--Samanta claims that a tensor family is a controlled \(g\)-fusion frame if and only if both factor families are controlled \(g\)-fusion frames. Under the paper's printed definition this is false.

For the first factor define
\[
q_H(f)=
\sum_{i\in I}v_i^2
\langle \Lambda_iP_{V_i}Uf,\Lambda_iP_{V_i}Tf\rangle,
\]
and define \(q_K(g)\) analogously for the second factor. The tensor energy on a simple tensor \(f\otimes g\) factors exactly as
\[
q_H(f)q_K(g).
\]
The paper permits arbitrary bounded invertible controls. Therefore the two factor energies can both be negative even though their product is positive.

Take
\[
H=K=\mathbb R
\]
with one relay-free \(g\)-fusion block in each factor:
\[
V_1=H,\qquad W_1=K,\qquad
\Lambda_1=I_H,\qquad \Gamma_1=I_K,
\qquad v_1=w_1=1.
\]
Choose
\[
T=T_1=I,\qquad U=U_1=-I.
\]
Then
\[
q_H(f)=-|f|^2,\qquad
q_K(g)=-|g|^2.
\]
Neither factor is a controlled \(g\)-fusion frame.

On the tensor product, however,
\[
T\otimes T_1=I,\qquad
U\otimes U_1=I,
\]
so the tensor family is Parseval:
\[
q_{H\otimes K}(f\otimes g)=|f\otimes g|^2.
\]
Thus the reverse implication of Theorem 4 fails in the smallest possible nontrivial model.

A sufficient repair is to require the two factor controlled quadratic forms to be real and nonnegative. Under that additional hypothesis, the source's division argument becomes valid and yields two-sided frame bounds for each factor.

## Assumptions and scope
The source defines
\[
GB(H)
\]
as the bounded invertible operators on \(H\) and separately defines
\[
GB^+(H)
\]
as the positive invertible operators. Its controlled \(g\)-fusion-frame definition assumes only
\[
T,U\in GB(H),
\]
and the tensor-product definition likewise assumes
\[
T,U\in GB(H),\qquad T_1,U_1\in GB(K).
\]
The counterexample uses exactly those printed hypotheses.

Real one-dimensional spaces are used so that every displayed controlled energy is an ordinary real scalar and every tensor vector is simple. There are no convergence, measurability, domain, or closure issues.

The result concerns the reverse implication in Theorem 4. The forward implication from two genuine factor controlled frames to the tensor frame remains valid.

## Proof
With one block, identity analysis maps, unit weights, and \(U=-I\), \(T=I\),
\[
q_H(f)
=
\langle -f,f\rangle
=
-|f|^2.
\]
For every \(f\ne0\) this is negative, so there cannot exist a positive constant \(A_H\) such that
\[
A_H|f|^2\le q_H(f).
\]
The same calculation gives
\[
q_K(g)=-|g|^2.
\]
Hence neither factor satisfies the source's controlled-frame definition.

Tensoring the controls gives
\[
(-I)\otimes(-I)=I,\qquad I\otimes I=I.
\]
The tensor family has one identity block and therefore
\[
q_{H\otimes K}(f\otimes g)
=
\langle f\otimes g,f\otimes g\rangle
=
\|f\otimes g\|^2.
\]
It is a Parseval controlled \(g\)-fusion frame. This directly contradicts the claimed equivalence.

For the repaired reverse implication, suppose
\[
q_H(f)\ge0,\qquad q_K(g)\ge0
\]
for all vectors and suppose the tensor family has bounds \(A,B\). The factorization of the tensor energy gives, for all nonzero \(f,g\),
\[
A\|f\|^2\|g\|^2
\le
q_H(f)q_K(g)
\le
B\|f\|^2\|g\|^2.
\]
The lower inequality implies both factors are strictly positive on nonzero vectors.

Fix \(g_0\ne0\). Division by the positive scalar \(q_K(g_0)\) gives
\[
\frac{A\|g_0\|^2}{q_K(g_0)}\|f\|^2
\le q_H(f)\le
\frac{B\|g_0\|^2}{q_K(g_0)}\|f\|^2.
\]
Thus the first factor is a controlled \(g\)-fusion frame. Fixing \(f_0\ne0\) gives the same conclusion for the second factor.

Conversely, if the factors have positive bounds \(A_H,B_H\) and \(A_K,B_K\), multiplying their inequalities gives tensor bounds
\[
A_HA_K,\qquad B_HB_K.
\]
Thus the published equivalence is restored under the added factor-positivity hypothesis.

In the real-valued setting the tensor inequality itself forces a sign dichotomy. Fix nonzero \(g_0\). Since
\[
q_H(f)q_K(g_0)>0
\]
for every nonzero \(f\), all nonzero values of \(q_H\) have the sign of \(q_K(g_0)\). The same argument interchanging factors shows that both forms have the same constant sign. The theorem captures only the positive branch; the counterexample realizes the negative branch.

## Verification
The primary publisher PDF was inspected at the definitions of \(GB(H)\) and \(GB^+(H)\), the controlled \(g\)-fusion-frame definition, the tensor-product controlled-frame definition, Theorem 4, and the complete proof of its reverse implication.

The printed definition uses \(T,U\in GB(H)\), not \(GB^+(H)\). Theorem 4 repeats the arbitrary-invertible hypothesis for both tensor factors.

In the reverse proof, the tensor inequality is factored into the product of the two factor energies. The proof notes only that each factor is nonzero, then divides by one factor to manufacture lower and upper bounds for the other. This step preserves the inequality orientation only when the denominator is positive.

The source's worked example later chooses positive controls, but that example does not add positivity to the theorem's hypotheses.

The counterexample and the repaired proof are exact symbolic calculations.

## Relationship to prior work
The source cites Liu--Huang--Zhu, *Controlled \(g\)-fusion frame in Hilbert space*, as its controlled-frame precursor. The present result does not depend on changing that definition; it uses the tensor paper's own explicit \(GB(H)\) hypotheses.

Ghosh--Samanta's contemporaneous preprint *Continuous controlled generalized fusion frames in Hilbert spaces*, arXiv:2110.11234v1, likewise distinguishes \(GB(H)\) from \(GB^+(H)\) and states its controlled \(g\)-fusion-frame definition for \(T,U\in GB(H)\). This confirms that arbitrary invertible controls are not merely a typographical shorthand unique to Theorem 4.

Ordinary fusion-frame and \(g\)-frame tensor-product theorems use nonnegative norm-square energies, so their factorization arguments do not have this sign obstruction.

Exact-title, DOI, theorem-number, negative-control, tensor-sign, and correction searches did not locate an indexed erratum or a checked source containing this counterexample or the factor-positivity repair.

## Limitations
The counterexample addresses Theorem 4 under the printed arbitrary-invertible-control convention. If one replaces the definition globally by a convention that independently guarantees nonnegative controlled energies, the obstruction disappears.

The nonnegativity hypothesis stated above is a clean sufficient repair, not a claim that positivity of each individual control operator is by itself necessary or sufficient in every noncommutative configuration.

Over complex Hilbert spaces, arbitrary controlled quadratic forms can carry phases rather than only signs. The one-dimensional real counterexample is enough to refute the theorem, and no complete complex-phase classification is claimed here.

## References
1. P. Ghosh and T. K. Samanta, *Controlled generalized fusion frame in the tensor product of Hilbert spaces*, Armenian Journal of Mathematics 13(13) (2021), 1--18, DOI 10.52737/18291163-2021.13.13-1-18.
2. P. Ghosh and T. K. Samanta, *Continuous controlled generalized fusion frames in Hilbert spaces*, arXiv:2110.11234v1, 4 October 2021.
3. H. Liu, Y. Huang and F. Zhu, *Controlled \(g\)-fusion frame in Hilbert space*, International Journal of Wavelets, Multiresolution and Information Processing 19(5) (2021), Article 2150009, DOI 10.1142/S0219691321500090.
