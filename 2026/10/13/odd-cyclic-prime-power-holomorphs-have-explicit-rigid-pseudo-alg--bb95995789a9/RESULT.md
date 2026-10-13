# Odd cyclic prime-power holomorphs have explicit rigid pseudo-algebras

## Finding

Let
\[
p
\]
be an odd prime and let
\[
n\ge2.
\]
Put
\[
G_{p,n}
=
\operatorname{Hol}(C_{p^n})
=
C_{p^n}\rtimes(\mathbb Z/p^n\mathbb Z)^\times.
\]

For an irreducible character \(\chi\), write
\[
\operatorname{cod}(\chi)
=
\frac{|G_{p,n}:\ker\chi|}{\chi(1)}.
\]
If \(m_G(d)\) denotes the number of irreducible characters of codegree \(d\), then
\[
\boxed{
\begin{aligned}
C(G_{p,n})
={}&
\{(1,1)\}\\
&\cup
\{(p^t,p^t):1\le t\le n-1\}\\
&\cup
\{(p^n,p^{n-1})\}\\
&\cup
\{(e p^s,\varphi(e)\varphi(p^s)):
e\mid p-1,\ e>1,\ 0\le s\le n-1\}.
\end{aligned}
}
\]

In particular, within the family of odd cyclic prime-power holomorphs,
\[
\boxed{
C(G_{p,n})=C(G_{q,m})
\iff
(p,n)=(q,m).
}
\]

Indeed, the largest codegree is
\[
p^n,
\]
and its multiplicity is
\[
p^{n-1}.
\]
Their ratio is \(p\), so the pseudo-algebra recovers the prime. The largest codegree then recovers \(n\).

The boundary \(n=1\) is the affine Frobenius group
\[
\operatorname{Hol}(C_p)\cong\operatorname{AGL}_1(\mathbf F_p);
\]
the result here starts at \(n=2\), where the holomorph is no longer a Frobenius group and the \(p\)-part of the automorphism group creates the new codegree layers.

## Assumptions and scope

The group pseudo-algebra is the codegree-multiplicity set
\[
C(G)=\{(d,m_G(d)):d\in\operatorname{Cod}(G)\}.
\]

Only odd primes are treated. For \(p=2\), the automorphism group of \(C_{2^n}\) is not cyclic once \(n\ge3\), and the irreducible-representation parametrization has additional branches.

The theorem is internal to the family
\[
\{\operatorname{Hol}(C_{p^n}):p\text{ odd},\ n\ge2\}.
\]
It does not assert that an arbitrary finite group with the same pseudo-algebra is a cyclic prime-power holomorph.

## Proof

Put
\[
N=p^n
\]
and
\[
M=\varphi(p^n)=p^{n-1}(p-1).
\]
For odd \(p\), the automorphism group of \(C_{p^n}\) is cyclic, so
\[
G_{p,n}
=
\langle a,b\mid
a^{p^n}=1,\ 
b^M=1,\ 
b^{-1}ab=a^r
\rangle,
\]
where \(r\) has multiplicative order \(M\) modulo \(p^n\).

The known complex irreducible representations split into one linear family and \(n\) nonlinear strata.

The linear characters kill \(a\) and send \(b\) to an arbitrary \(M\)-th root of unity. Therefore a linear character of exact order \(d\mid M\) has codegree \(d\), and there are
\[
\varphi(d)
\]
such characters.

Now fix
\[
1\le k\le n.
\]
The nonlinear stratum indexed by \(k\) consists of
\[
p^{n-k}
\]
irreducible representations
\[
\rho_{k,\omega}
\]
of degree
\[
d_k=\varphi(p^k)=p^{k-1}(p-1),
\]
where \(\omega\) runs through the \(p^{n-k}\)-th roots of unity.

Let \(\omega\) have exact order
\[
p^s,
\qquad
0\le s\le n-k.
\]
In the standard monomial realization, \(\rho_{k,\omega}(a)\) is diagonal with diagonal entries
\[
\xi,\ \xi^r,\ \xi^{r^2},\ldots,
\]
where \(\xi\) is a primitive \(p^k\)-th root of unity, while \(\rho_{k,\omega}(b)\) is a cyclic shift of length \(d_k\) whose wrap-around scalar is \(\omega\). Hence
\[
\rho_{k,\omega}(b)^{d_k}
=
\omega I.
\]

Consider
\[
a^x b^y.
\]
If it lies in the kernel, the permutation part of the monomial matrix forces
\[
d_k\mid y.
\]
Write
\[
y=d_k z.
\]
The matrix then becomes the diagonal matrix from \(a^x\), multiplied by the scalar \(\omega^z\).

Comparing the first two diagonal entries shows
\[
\xi^{(r-1)x}=1.
\]
Because \(r\) is primitive modulo \(p\) and \(p\) is odd,
\[
p\nmid r-1.
\]
Thus
\[
p^k\mid x.
\]
The entire \(a\)-matrix is then the identity, and the remaining condition is
\[
\omega^z=1,
\]
equivalently
\[
p^s\mid z.
\]

Therefore
\[
|\ker\rho_{k,\omega}|
=
p^{n-k}\,p^{n-k-s}
=
p^{2(n-k)-s}.
\]
Since
\[
|G_{p,n}|=p^{2n-1}(p-1),
\]
the codegree is
\[
\frac{|G_{p,n}|}{|\ker\rho_{k,\omega}|\,\rho_{k,\omega}(1)}
=
p^{k+s}.
\]

For a fixed
\[
t,\qquad1\le t\le n,
\]
the nonlinear characters of codegree \(p^t\) arise from
\[
k+s=t.
\]
For every \(s\), there are
\[
\varphi(p^s)
\]
choices of \(\omega\) of exact order \(p^s\). Hence the nonlinear multiplicity is
\[
\sum_{s=0}^{t-1}\varphi(p^s)
=
p^{t-1}.
\]

For
\[
1\le t\le n-1,
\]
the linear characters contribute another
\[
\varphi(p^t)=p^{t-1}(p-1)
\]
characters of codegree \(p^t\). Thus the total multiplicity is
\[
p^{t-1}+p^{t-1}(p-1)
=
p^t.
\]
At the top codegree \(p^n\), no linear character contributes, so its multiplicity is \(p^{n-1}\).

Finally, every divisor of
\[
M=p^{n-1}(p-1)
\]
has a unique form
\[
e p^s,
\qquad
e\mid p-1,\quad0\le s\le n-1.
\]
If \(e>1\), this codegree arises only from linear characters, with multiplicity
\[
\varphi(e p^s)=\varphi(e)\varphi(p^s).
\]
This proves the displayed pseudo-algebra.

Among all listed codegrees,
\[
p^n
\]
is largest, because
\[
e p^s\le(p-1)p^{n-1}<p^n.
\]
Its multiplicity is \(p^{n-1}\). Therefore
\[
p
=
\frac{p^n}{p^{n-1}}
\]
is reconstructed from the pseudo-algebra, and then \(n\) is reconstructed from the largest codegree.

## Verification

The included checker independently enumerates every irreducible-representation parameter in the known monomial parametrization.

For each odd prime
\[
p\in\{3,5,7,11\}
\]
and each
\[
2\le n\le5,
\]
it enumerates:

- every linear character of the cyclic quotient of order
  \[
  \varphi(p^n);
  \]
- every nonlinear pair
  \[
  (k,\omega),
  \qquad
  1\le k\le n,
  \]
  with \(\omega\) a \(p^{n-k}\)-th root parameter.

For the nonlinear representations it computes the order of \(\omega\), the kernel size
\[
p^{2(n-k)-s},
\]
the degree
\[
\varphi(p^k),
\]
and the resulting codegree directly. It then compares the accumulated multiplicities with the closed formula.

It also verifies the character degree-squared identity
\[
\sum_{\chi\in\operatorname{Irr}(G_{p,n})}\chi(1)^2
=
|G_{p,n}|
\]
and reconstructs \(p\) and \(n\) from the top codegree and its multiplicity.

For
\[
G_{3,2}=\operatorname{Hol}(C_9),
\]
the checker obtains
\[
C(G_{3,2})
=
\{(1,1),(2,1),(3,3),(6,2),(9,3)\}.
\]

The checker returns `VERIFY_OK`.

The finite checks are consistency tests; the all-\(p\), all-\(n\) theorem is proved symbolically.

## Relationship to prior work

Pradhan and Sury explicitly determine all complex irreducible representations of
\[
\operatorname{Hol}(C_{p^n}).
\]
For odd \(p\), their Theorem 6.0.1 gives the linear characters and, for every \(1\le k\le n\), exactly \(p^{n-k}\) nonlinear irreducibles of degree
\[
\varphi(p^k),
\]
together with the explicit monomial matrices used in the proof above. Their paper studies faithful permutation and quasi-permutation representation degrees and rational Wedderburn decompositions; its full searchable text contains no occurrence of “codegree” or “pseudo-algebra”.

Moretó introduced the group pseudo-algebra and asked how much group structure this invariant remembers. Lewis and Yan later exhibited global order collisions and proved rigidity under additional hypotheses. The inspected texts contain no holomorph specialization.

The boundary
\[
n=1
\]
is a scalar affine Frobenius group and is already covered by the known pseudo-algebra formula for that Frobenius family. The present theorem begins at
\[
n=2,
\]
where the cyclic automorphism group has a nontrivial \(p\)-part and the nonlinear codegree tower
\[
p,\ p^2,\ldots,p^n
\]
is genuinely new.

Targeted searches under holomorph, metacyclic, cyclic prime-power, character-codegree, and pseudo-algebra formulations did not locate the displayed formula.

## Limitations

The restriction to odd primes is essential to the proof as written. The \(2\)-power holomorph has a noncyclic automorphism group for \(n\ge3\) and requires a separate representation analysis.

The irreducible-representation parametrization itself is prior work. The new content is the exact kernel and codegree calculation, its aggregation into a closed pseudo-algebra, and the resulting family-internal rigidity theorem.

The theorem proves rigidity only within the cyclic odd-prime-power holomorph family.

Failed searches do not prove novelty.

## References

1. S. S. Pradhan and B. Sury, “Rational and Quasi-Permutation Representations of Holomorph of Cyclic \(p\)-Groups,” arXiv:2106.12781v1, first public version 24 June 2021; *International Journal of Group Theory* 11 (2022), 151–174, DOI 10.22108/ijgt.2021.128359.1686. The preprint lists MSC 20CXX.
2. A. Moretó, “Multiplicities of character codegrees of finite groups,” *Bulletin of the London Mathematical Society* 55 (2023), 234–241, first published online 8 September 2022, DOI 10.1112/blms.12724.
3. M. L. Lewis and Q. Yan, “On the group pseudo-algebra of finite groups,” arXiv:2402.12648v1, first public version 20 February 2024; *Comptes Rendus. Mathématique* 362 (2024), 1661–1665, DOI 10.5802/crmath.671.
