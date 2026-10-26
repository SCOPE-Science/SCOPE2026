# All-genus orbit series for elementary abelian eightfold covers

## Finding
Let \(G=(\mathbb Z/2\mathbb Z)^3\), and let \(a_r\) count topological-equivalence classes of faithful orientation-preserving \(G\)-actions on smooth connected compact complex curves with quotient \(\mathbb P^1\) and exactly \(r\) branch points, all with inertia group of order \(2\). For every \(r\ge5\), the curves have genus \(g=2r-7\ge3\). Write
\[
P(t)=1+t^2-t^5-t^7+2t^8-t^9+t^{10}+t^{11}+t^{13}-t^{14}-t^{15}+t^{16}.
\]
Then, with the formal combinatorial boundary value \(a_4=1\) (genus one), the **entire sequence** has rational generating function
\[
\boxed{\sum_{r\ge4}a_rt^r=\frac{t^4P(t)}{(1-t)^7(1+t)^4(1+t^2)^2(1-t+t^2)(1+t+t^2)^2(1+t+t^2+t^3+t^4+t^5+t^6)}.}
\]
The coefficients for \(r=4,\ldots,20\) are
\[
1,1,3,4,8,9,17,20,34,39,61,72,106,123,174,204,277.
\]
In particular, \(a_r\sim r^6/967680\). This is a topological classification count for **all branch lengths**, not an enumeration restricted to low genera.

## Assumptions and scope
The ground field is \(\mathbb C\), and equivalence permits orientation-preserving homeomorphisms of the curve together with automorphisms of \(G\). Branch points are unlabelled; their inertia orders are all \(2\), but their individual nonzero inertia elements need not agree. The group action is faithful, hence the branch monodromies generate \(G\). No assertion is made about isomorphism classes of algebraic curves or the full automorphism group of a curve.

## Proof
Write \(V=\mathbb F_2^3\) and \(V^\times=V\setminus\{0\}\). The Riemann existence theorem identifies covers of the stated signature with tuples \((v_1,\ldots,v_r)\in(V^\times)^r\) satisfying \(v_1+\cdots+v_r=0\) and \(\langle v_1,\ldots,v_r\rangle=V\). Because \(V\) is abelian, the Hurwitz braid generators simply interchange adjacent tuple entries. Quotienting further by \(\operatorname{Aut}(V)=\operatorname{GL}_3(\mathbb F_2)\) therefore identifies equivalence classes precisely with its orbits on **spanning, zero-sum multisets** of size \(r\) drawn from the seven nonzero points of the Fano plane. Riemann–Hurwitz gives \(2g-2=8(-2+r/2)\), hence \(g=2r-7\).

For \(g_0\in\operatorname{GL}_3(\mathbb F_2)\), let \(\mathcal C(g_0)\) be its cycles on \(V^\times\). A fixed multiset assigns constant multiplicity \(n_C\ge0\) to each cycle \(C\). If its support lies in a subspace \(U\le V\), then only cycles fully contained in \(U\) can occur; denote these by \(\mathcal C_U(g_0)\). Write \(n_C=\epsilon_C+2k_C\), where \(\epsilon_C\in\{0,1\}\). The zero-sum condition is
\[
\bigoplus_{C\in\mathcal C_U(g_0)}\epsilon_C\Bigl(\bigoplus_{v\in C}v\Bigr)=0.
\]
Thus the generating series of fixed zero-sum multisets supported in \(U\) is the explicitly finite rational expression
\[
Q_{g_0,U}(t)=\frac{\displaystyle\sum_{\epsilon\in\{0,1\}^{\mathcal C_U(g_0)}\atop\oplus_C\epsilon_C\oplus_{v\in C}v=0}t^{\sum_C\epsilon_C|C|}}{\displaystyle\prod_{C\in\mathcal C_U(g_0)}(1-t^{2|C|})}.
\]
The Möbius function of the lattice of subspaces of \(V\) is \(\mu(U,V)=(-1)^c2^{\binom c2}\), for \(c=3-\dim U\). Inverting the span condition, the series for \(g_0\)-fixed spanning zero-sum multisets is
\[
F_{g_0}(t)=\sum_{U\le V}\mu(U,V)Q_{g_0,U}(t).
\]
There are exactly sixteen subspaces, with dimension distribution \(1,7,7,1\). On the seven nonzero vectors, the \(168\) matrices of \(\operatorname{GL}_3(\mathbb F_2)\) have exactly the following cycle-type/count distribution:
\[
\begin{array}{c|ccccc}\text{cycle lengths}&1^7&1^3 2^2&1\,2\,4&1\,3^2&7\\\hline\text{number}&1&21&42&56&48\end{array}.
\]
Burnside's lemma now gives
\[
H(t)=\frac1{168}\sum_{g_0\in\operatorname{GL}_3(\mathbb F_2)}F_{g_0}(t).
\]
Substituting the five types, evaluating the parity-constrained numerator sums, and combining the denominators yields precisely the boxed rational function. The file `verify_orbit_series.py` gives an exact *bounded polynomial identity certificate* for this last simplification: a common denominator for all five class contributions is
\[
E(t)=\prod_{\text{five types }\tau}\ \prod_{C\in\mathcal C(g_\tau)}(1-t^{2|C|}),\qquad\deg E=70.
\]
Each restricted-subspace denominator divides its type's full-cycle factor, so \(E(t)H(t)\) is a polynomial of degree at most \(70\). The proposed denominator of degree \(27\) divides \(E\), while the proposed numerator has degree \(20\), making its product with \(E\) a polynomial of degree \(63\). Exact matching of coefficients through degree \(70\) therefore **proves equality of the two rational functions**, rather than sampling an infinite claim.

For the asymptotic, only the identity cycle type can have a pole of order seven at \(t=1\). Its zero-sum parity numerator over all seven points is the Hamming-code weight enumerator \(1+7t^3+7t^4+t^7\), with value \(16\) at \(1\), and its denominator is \((1-t^2)^7\). Proper-subspace corrections have poles of order at most three at \(1\). Hence \(H(t)\sim(1344(1-t)^7)^{-1}\) at \(t=1\). At \(t=-1\) the numerator \(1+7t^3+7t^4+t^7\) vanishes, so the pole order is strictly below seven; all other roots of unity likewise have smaller pole orders. Therefore coefficient extraction gives \(a_r\sim r^6/(1344\cdot 6!)=r^6/967680\).

## Verification
Run `python3 verify_orbit_series.py` with Python 3.9+; no third-party packages are needed. The checker enumerates all \(168\) invertible binary matrices, verifies their five cycle-type cardinalities and all sixteen subspaces, evaluates the five Burnside–Möbius rational coefficient series exactly, and performs polynomial division to verify that the claimed degree-\(27\) denominator divides the explicit degree-\(70\) common denominator. It then compares all \(71\) required coefficients, proving the rational identity by the polynomial degree bound. A separate full group-orbit enumeration confirms \(a_r\) for each \(3\le r\le12\). The run output is:

```
VERIFY_OK GL3_order=168 conjugacy_types=5 subspaces=16 denominator_degree=70
VERIFY_OK rational_identity_exact=true coefficients_0_to_70=true independent_orbits_r3_to_r12=true
first_coefficients [1, 1, 3, 4, 8, 9, 17, 20, 34, 39, 61, 72, 106, 123, 174, 204, 277]
```

## Relationship to prior work
Broughton and Wootton (2007) give general methods for elementary abelian surface-action classification and work out the three-/four-branch-point cases; in particular, their rank-three, four-branch-point count agrees with \(a_4=1\). Weaver (2017) counts zero-sum multisets for rank-two elementary abelian groups over *odd* prime fields. Both the general orbit-counting framework and the zero-sum multiset approach are credited as established techniques. Disney-Hogg and Zuev (2026) study the equivalence decision problem computationally using generating-vector datasets limited to genus \(48\); their paper motivates an exact all-genus benchmark but does not give this rank-three binary rational series. The assessed new fact is the complete explicit function and associated asymptotic, not the underlying general classification method.

## Limitations
The formula concerns only the specified group, quotient genus zero and inertia-two signature; it is not an enumeration of all groups acting on curves. The degree-\(70\) identity check is a complete finite certificate for the rational simplification, not an empirical substitute for rationality: rationality and the denominator bound are established symbolically by the preceding Burnside–Möbius proof. Prior methods might yield the formula implicitly; no assertion of exhaustive historical priority is made. Independent mathematical validation has not been performed.

## References
1. L. Disney-Hogg and M. Zuev, *Deep Learning of Topological Equivalence Classes* (2026), arXiv:2610.21981v1, https://arxiv.org/html/2610.21981v1 .
2. S. A. Broughton and A. Wootton, *Finite abelian subgroups of the mapping class group*, Algebraic & Geometric Topology 7 (2007), 1651–1697, https://msp.org/agt/2007/7-4/agt-v7-n4-p02-p.pdf .
3. A. Weaver, *Zero-sum multisets mod p with an application to surface automorphisms* (2017), arXiv:1703.02147, https://arxiv.org/abs/1703.02147 .
4. J. Paulhus, *Branching data for curves up to genus 48* (2015), http://www.jenpaulhus.com/research/monodromy.html (historical finite-genus data cited in Reference 1).
