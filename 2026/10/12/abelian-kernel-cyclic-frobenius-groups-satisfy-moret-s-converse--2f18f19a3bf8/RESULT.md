# Abelian-kernel cyclic Frobenius groups satisfy Moretó's converse

## Finding

Let
\[
G=K\rtimes H
\]
be a finite Frobenius group with nontrivial abelian kernel \(K\) and cyclic complement
\[
H\cong C_m,
\qquad
m>1.
\]
For
\[
\chi\in\operatorname{Irr}(G),
\]
write
\[
\operatorname{cod}(\chi)
=
\frac{|G:\ker\chi|}{\chi(1)}.
\]

Every irreducible character belongs to exactly one of two families.

If
\[
K\le\ker\chi,
\]
then \(\chi\) is inflated from a linear character of \(H\), and
\[
\boxed{
\operatorname{cod}(\chi)
=
|H:\ker(\chi|_H)|
\mid m.
}
\]

Otherwise there is a nonprincipal
\[
\theta\in\operatorname{Irr}(K)
\]
such that
\[
\chi=\theta^G.
\]
Put
\[
N_\theta
=
\bigcap_{h\in H}\ker(\theta^h).
\]
Then
\[
\boxed{
\chi(1)=m,
\qquad
\ker\chi=N_\theta,
\qquad
\operatorname{cod}(\chi)=|K:N_\theta|.
}
\]

Thus every codegree lives entirely on one side of the Frobenius decomposition: an inflated-character codegree divides \(|H|\), while an induced-character codegree divides \(|K|\).

More strongly, for every irreducible character \(\chi\) there exists an element \(g\in G\) such that
\[
\boxed{
\pi(\operatorname{cod}(\chi))
=
\pi(o(g)).
}
\]
If \(\chi\) is inflated from \(H\), one may choose \(g\in H\) with
\[
o(g)=\operatorname{cod}(\chi).
\]
If \(\chi=\theta^G\), one may choose \(g\in K\) of squarefree order
\[
\prod_{\ell\mid\operatorname{cod}(\chi)}\ell.
\]

Consequently, Moretó's converse relation between character codegrees and element orders has an affirmative answer throughout the family of Frobenius groups with abelian kernel and cyclic complement.

## Assumptions and scope

A Frobenius decomposition
\[
G=K\rtimes H
\]
means that every nonidentity element of \(H\) acts fixed-point-freely on
\[
K\setminus\{1\}.
\]

The theorem assumes that the kernel \(K\) is abelian and the complement \(H\) is cyclic. No elementary-abelian, prime-power, or irreducibility assumption is imposed on \(K\).

The conclusion is stronger than the containment asked for in Moretó's question: the witnessing element can be chosen so that the prime support of its order equals, rather than merely contains, the prime support of the character codegree.

The theorem does not claim the same conclusion for Frobenius groups with nonabelian kernels or noncyclic complements.

## Proof

Because \(K\) is abelian, every member of
\[
\operatorname{Irr}(K)
\]
is linear.

We first show that the complement acts semiregularly on the nonprincipal characters of \(K\). Let
\[
1\ne h\in H
\]
and suppose
\[
\theta^h=\theta
\]
for some
\[
\theta\in\operatorname{Irr}(K).
\]
Then
\[
\theta(k^{-1}k^h)=1
\]
for every \(k\in K\).

Since \(K\) is abelian, the map
\[
\delta_h:K\to K,
\qquad
\delta_h(k)=k^{-1}k^h,
\]
is a homomorphism. Its kernel is
\[
C_K(h)=1
\]
by the Frobenius property. Because \(K\) is finite, \(\delta_h\) is therefore bijective. Hence
\[
\ker\theta=K,
\]
so \(\theta\) is principal.

It follows that every nonprincipal character of \(K\) has an \(H\)-orbit of size \(m\).

Let
\[
1_K\ne\theta\in\operatorname{Irr}(K).
\]
Mackey's inner-product formula, or equivalently Frobenius reciprocity applied to the restriction of \(\theta^G\), gives
\[
\langle\theta^G,\theta^G\rangle_G
=
|\operatorname{Stab}_H(\theta)|
=
1.
\]
Thus
\[
\theta^G
\]
is irreducible and has degree
\[
[G:K]=m.
\]
Two such induced characters are equal exactly when their inducing characters lie in the same \(H\)-orbit.

There are therefore
\[
\frac{|K|-1}{m}
\]
distinct irreducible characters of this form. In addition, the \(m\) characters of the cyclic quotient
\[
G/K\cong H
\]
inflate to \(m\) linear irreducible characters of \(G\).

These characters exhaust \(\operatorname{Irr}(G)\), because their degree squares sum to
\[
m
+
\frac{|K|-1}{m}m^2
=
m|K|
=
|G|.
\]

Now consider an inflated character \(\chi\). Since \(H\) is cyclic, \(\chi|_H\) is linear, and
\[
\operatorname{cod}(\chi)
=
|H:\ker(\chi|_H)|.
\]
This number is the exact order of the character \(\chi|_H\), hence divides \(m\). A cyclic group contains an element of every order dividing its order, so there is
\[
g\in H
\]
with
\[
o(g)=\operatorname{cod}(\chi).
\]

Next let
\[
\chi=\theta^G
\]
with \(\theta\ne1_K\). Its restriction to \(K\) is
\[
\chi_K
=
\sum_{h\in H}\theta^h.
\]
Outside \(K\), an induced character from the normal Frobenius kernel has value zero, so no element of
\[
G\setminus K
\]
lies in \(\ker\chi\).

For \(k\in K\), all summands
\[
\theta^h(k)
\]
are complex roots of unity. Since
\[
\chi(1)=m,
\]
the equality
\[
\chi(k)=m
\]
holds exactly when every summand equals \(1\). Hence
\[
\ker\chi
=
\bigcap_{h\in H}\ker(\theta^h)
=
N_\theta.
\]
Therefore
\[
\operatorname{cod}(\chi)
=
\frac{|G:N_\theta|}{m}
=
|K:N_\theta|.
\]

In particular, every prime divisor of this codegree divides \(|K|\). Since \(K\) is a finite abelian group, its Sylow subgroups commute. For each prime
\[
\ell\mid\operatorname{cod}(\chi),
\]
choose an element
\[
g_\ell\in K
\]
of order \(\ell\). Then
\[
g=\prod_{\ell\mid\operatorname{cod}(\chi)}g_\ell
\]
has squarefree order
\[
o(g)
=
\prod_{\ell\mid\operatorname{cod}(\chi)}\ell.
\]
Thus
\[
\pi(o(g))
=
\pi(\operatorname{cod}(\chi)).
\]

This proves the theorem.

## Verification

The included replay models finite abelian kernels explicitly and checks fixed-point-free cyclic actions, the dual-character orbits, the kernels
\[
N_\theta,
\]
the resulting induced-character codegrees, and the required element-order witnesses.

The verified Frobenius examples are
\[
C_9\rtimes C_2,
\qquad
C_{15}\rtimes C_2,
\qquad
(C_3\times C_3)\rtimes C_4,
\]
\[
(C_5\times C_5)\rtimes C_3,
\qquad
(C_3\times C_9)\rtimes C_2,
\qquad
(C_5\times C_{25})\rtimes C_4.
\]

The examples include cyclic, noncyclic, elementary-abelian, and non-elementary-abelian kernels, as well as complements of orders \(2\), \(3\), and \(4\).

For every nonprincipal kernel character, the replay verifies that its complement orbit has full length, computes
\[
|K:N_\theta|,
\]
and finds a kernel element whose order has exactly the same prime support. It also verifies the degree-squared completeness identity
\[
m+\frac{|K|-1}{m}m^2
=
m|K|.
\]

The replay returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.

## Relationship to prior work

Jin, Wang, and Yang study Moretó's proposed converse between character codegrees and element orders. Their public preprint states the question explicitly and constructs solvable counterexamples by producing faithful primitive characters whose codegrees involve more primes than any element order can contain. The resulting counterexample construction uses nonabelian extraspecial Fitting subgroups.

The theorem above identifies a large positive Frobenius regime on the other side of that obstruction. With an abelian kernel and a cyclic complement, irreducible characters split completely into complement-inflated characters and kernel-induced characters. Their codegrees consequently stay on one side of the Frobenius decomposition, and an element-order witness can be chosen on that same side.

A corrigendum on groups with three codegrees proves that a Frobenius group with exactly three codegrees has elementary abelian derived subgroup. That theorem concerns a highly restricted codegree-set size and does not give the arbitrary cyclic-complement statement or the codegree-to-element-order witnesses proved here.

Searches using Moretó's question, Frobenius groups, abelian kernels, cyclic complements, codegree prime support, and induced-character formulations did not locate the displayed theorem.

## Limitations

The abelian-kernel hypothesis is essential to the proof: it makes every kernel character linear and turns the fixed-point-free action on \(K\) into a semiregular action on its nonprincipal dual characters.

The cyclic-complement hypothesis is used to realize every inflated-character codegree as an exact complement element order. The proof does not assert that an arbitrary Frobenius complement has the corresponding property.

The theorem concerns prime support, as in Moretó's question. For induced characters, the codegree
\[
|K:N_\theta|
\]
need not itself occur as an element order of \(K\).

A scalar affine Frobenius group is a special case, but the theorem allows arbitrary finite abelian Frobenius kernels, including non-elementary kernels.

Failed searches do not prove novelty.

## References

1. P. Jin, L. Wang, and Y. Yang, “Codegrees of primitive characters of solvable groups,” arXiv:2111.00133v1, first public version 30 October 2021; published as “On a question of Moretó,” *Bulletin of the Australian Mathematical Society* 106 (2022), 306–309, DOI 10.1017/S0004972722000338. Primary MSC 20C15.
2. F. Alizadeh, H. Behravesh, M. Ghaffarzadeh, M. Ghasemi, and S. Hekmatara, “Corrigendum to: Groups with few codegrees of irreducible characters,” *Communications in Algebra* 50 (2022), 5479–5480, DOI 10.1080/00927872.2022.2087226.
