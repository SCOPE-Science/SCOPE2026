# Exact real-rootedness windows for prisms over empty lattice tetrahedra

## Finding
Let \(S\subset\mathbb R^3\) be any full-dimensional **empty lattice tetrahedron**: its only integer points are its four vertices. Let \(m=6\operatorname{vol}_3(S)\in\mathbb Z_{\ge1}\) be its normalized lattice volume, and let \(k\ge1\) be an integer. For the four-dimensional lattice prism \(Q=S\times[0,k]\), its Ehrhart numerator is
\[
 h_Q^*(z)=1+(4k-1)z+(m-1)(2k+1)z^2+(m-1)(2k-1)z^3.
\]
For \(m=1\), it has the single negative root \(-1/(4k-1)\). For \(m\ge2\), **all** its roots are real (and necessarily strictly negative) exactly when
\[
\boxed{\left(\frac{4k-1}{2k+1}\right)^3\le m-1\le2k-1.}\tag{1}
\]
The criterion has the following exact classification by normalized volume:

| \(m\) | Positive integer heights \(k\) for which all roots are real |
| --- | --- |
| \(1\) | every \(k\ge1\) |
| \(2\) | \(k=1\) |
| \(3\) | none |
| \(4\) | \(k=2\) |
| \(5\) | \(k=3\) |
| \(6\) | \(k=3,4\) |
| \(7\) | \(4\le k\le7\) |
| \(8\) | \(4\le k\le16\) |
| \(m\ge9\) | exactly \(k\ge\lceil m/2\rceil\) |

For \(m\ge2\) satisfying (1), the roots are simple unless \(m=2k\). On this equality boundary,
\[
 h_Q^*(z)=(1+z)(1+(2k-1)z)^2.
\]
In particular, at \((m,k)=(2,1)\) the root \(-1\) has multiplicity three; at the other boundary pairs it is a double root and a distinct simple root. Off criterion (1), the cubic has exactly one negative real root and one nonreal conjugate pair.

## Assumptions and scope
The polytope \(S\) is a three-dimensional simplex with integral vertices and **no other lattice points** in \(S\), including on its boundary. The Euclidean volume is computed in the standard lattice \(\mathbb Z^3\); \(m\) is the determinant-normalized volume. The prism is embedded in the product lattice \(\mathbb Z^3\times\mathbb Z\), with positive integral segment length \(k\). Roots are those of the actual Ehrhart numerator, not zeros artificially appended to make its degree four. Every integer \(m\ge1\) occurs: the Reeve simplex \(R_m=\operatorname{conv}\{(0,0,0),(1,0,0),(0,1,0),(1,1,m)\}\) is empty and has normalized volume \(m\).

## Proof
**1. The tetrahedral numerator depends only on volume.** In dimension three, the standard Ehrhart identities give \(h_0^*=1\), \(h_1^*=|S\cap\mathbb Z^3|-4\), \(h_3^*=|\operatorname{int}(S)\cap\mathbb Z^3|\), and \(\sum_j h_j^*=6\operatorname{vol}_3(S)=m\). Emptiness implies \(h_1^*=h_3^*=0\), hence
\[
 h_S^*(z)=1+(m-1)z^2.
\]
These identities require no classification of empty tetrahedra. The realization statement follows by direct examination of the four vertices of \(R_m\): the base cross-section at integer height \(z\), for \(0<z<m\), requires integer \(x,y\ge1\) and \(x+y\le1+z/m<2\), which is impossible; its bottom face is the unimodular triangle.

**2. Product transform.** Write \(H(z)=\sum_{n\ge0}|nS\cap\mathbb Z^3|z^n=h_S^*(z)/(1-z)^4\). Since \(nQ=nS\times[0,nk]\), its lattice-point enumerator is \((kn+1)|nS\cap\mathbb Z^3|\). Consequently,
\[
\sum_{n\ge0}|nQ\cap\mathbb Z^4|z^n=H(z)+kzH'(z).
\]
Multiplying by \((1-z)^5\) gives
\[
 h_Q^*(z)=(1+(4k-1)z)h_S^*(z)+kz(1-z)(h_S^*)'(z),
\]
which expands to the displayed cubic. For \(m=1\), it reduces to \(1+(4k-1)z\).

**3. Exact discriminant.** For \(m\ge2\), put \(a=m-1\ge1\). The discriminant of \(1+(4k-1)z+a(2k+1)z^2+a(2k-1)z^3\) factors as
\[
\Delta=4a(2k-1-a)\bigl(a(2k+1)^3-(4k-1)^3\bigr).
\]
The two sign-transition values in \(a\) are \(2k-1\) and \(r(k)=((4k-1)/(2k+1))^3\). They are correctly ordered because
\[
 (2k-1)(2k+1)^3-(4k-1)^3=16k(k-1)^3\ge0.
\]
For \(k=1\) both values equal one; for every \(k\ge2\), the inequality is strict. Thus \(\Delta\ge0\) is precisely (1). A real cubic has three real roots counting multiplicities exactly when its discriminant is nonnegative. Since all its coefficients are positive, it has no nonnegative real root, so all three real roots in that regime are strictly negative. When \(\Delta<0\), it has one real root and a nonreal pair, and the real root is negative.

**4. Integer phase diagram.** The rational function \((4k-1)/(2k+1)\) is strictly increasing for real \(k>0\), from one at \(k=1\), and stays below two. Its cube \(r(k)\) therefore strictly increases toward eight. For each integer \(a=1,\ldots,7\), the lower inequality \(r(k)\le a\), combined with the upper inequality \(k\ge(a+1)/2\), gives the listed finite ranges. The decisive integer boundaries are \(r(2)>2\), \(r(3)>3\), \(r(4)>4\), \(r(5)>5\), \(r(7)<6<r(8)\), and \(r(16)<7<r(17)\); also \(r(2)<3\), \(r(3)<4\), \(r(4)<5\), \(r(4)<6\), and \(r(4)<7\). All these comparisons are exact rational cubings. For every integer \(a\ge8\), the lower inequality holds automatically because \(r(k)<8\); then only \(2k-1\ge a\) remains, equivalent to \(k\ge\lceil m/2\rceil\).

The lower boundary \(a=r(k)\) is impossible for integers \(a\) and \(k\ge2\): a rational whose cube is an integer must itself be an integer, whereas \(1<(4k-1)/(2k+1)<2\). Therefore the discriminant vanishes at an integral pair only on \(a=2k-1\), or at \((a,k)=(1,1)\). Direct substitution yields \((1+z)(1+(2k-1)z)^2\), including the triple root for \(k=1\). This completes the classification.

## Verification
The accompanying standalone script `check.py` uses exact symbolic arithmetic to verify the numerator transform, an independent finite-difference Ehrhart inversion, the discriminant factorization, both polynomial identities used for the boundary, and the repeated-root factorization. It also counts lattice points directly by integral horizontal sections for 105 pairs \((m,n)\), and checks the integer phase diagram in 22,500 pairs \((m,k)\). Its observed output is:

```text
EMPTY_TETRA_PRISM_OK symbolic_identities=5 independent_lattice_counts= 105 parameter_pairs= 22500
```

The symbolic identities and preceding elementary argument prove the theorem for all allowed integers. The finite tests do not purport to establish an infinite classification by enumeration.

## Relationship to prior work
The Reeve family and its Ehrhart polynomial are classical; Liu, Tao, and Xin (2026) use it in a construction controlling signs of Ehrhart **coefficients**, not a sharp root-phase diagram for segment products [1]. Liu (2026), Section 2, gives Hadamard-product formulas and proves that products preserve \(h^*\)-real-rootedness **when both factors already have it** [2]. For \(m\ge2\), the tetrahedral numerator \(1+(m-1)z^2\) is not real-rooted, so the cited preservation theorem cannot imply the result here. Nill's large-lattice-width sufficient condition [3] cannot explain the width-one Reeve-based examples here. The exact dependence on both \(m\) and \(k\), its transient small-volume windows and permanent large-volume threshold, is not asserted in those inspected results. No claim of exhaustive historical priority is made.

## Limitations
The theorem concerns product prisms over **empty tetrahedra**; it gives no necessary-and-sufficient root criterion for arbitrary four-dimensional lattice polytopes or nonempty tetrahedral bases. The first literature date used for this study is the public submission of [1], May 22, 2026; later revisions do not change it. An equivalent classification in other or older literature may remain unindexed. The findings concern algebraic root locations, not lattice normality or unimodular triangulations. Independent scientific validation has not been performed.

## References
[1] F. Liu, S. Tao, G. Xin, *Explicit Construction of Polytopes whose Ehrhart Polynomials Realize any Given Sign Pattern*, arXiv:2605.23544 (first public May 22, 2026), especially the Reeve formula and Cartesian-product construction.

[2] F. Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338 (first public October 5, 2026), Section 2.

[3] B. Nill, *Lattice polytopes of large width have real-rooted Ehrhart \(h^*\)-polynomials*, arXiv:2608.03635 (first public August 4, 2026).

[4] J. E. Reeve, *On the volume of lattice polyhedra*, Proceedings of the London Mathematical Society (1957), 378–395.
