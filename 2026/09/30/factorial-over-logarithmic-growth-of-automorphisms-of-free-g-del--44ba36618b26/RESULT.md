# Factorial-over-logarithmic growth of automorphisms of free Gödel algebras

## Finding
Let \(G_n\) be the free \(n\)-generated Gödel algebra. Put \(L=\log 2\) and
\[
f_m=\sum_{j=0}^{m-1}\log\!\left(\binom{m}{j}!\right),\qquad
\Phi(z)=\sum_{m\ge 0} f_m\frac{z^m}{m!},\qquad
\kappa=\Phi(L).
\]
Then \(\Phi\) is entire and
\[
\log |\operatorname{Aut}(G_n)|=\kappa\frac{n!}{L^{n+1}}+O\!\left(n!R^{-n}\right)
\]
for every fixed \(R\) satisfying \(L<R<\sqrt{L^2+4\pi^2}\). In particular,
\[
\frac{L^{n+1}}{n!}\log|\operatorname{Aut}(G_n)|\longrightarrow\kappa
=0.5656527950551603024\ldots .
\]
All logarithms are natural.

## Assumptions and scope
The result uses the published finite-generator spectral-forest description and automorphism decomposition for free Gödel algebras. Let \(H_0\) be the empty forest and, for \(n\ge1\), let \(H_n\) be the disjoint union, over \(0\le j<n\), of \(\binom{n}{j}\) copies of the rooted forest obtained from \(H_j\) by adjoining a new minimum. The published decomposition identifies the automorphism group of the free \(n\)-generated Gödel algebra with the square of \(\operatorname{Aut}(H_n)\).

## Proof
Write \(h_n=|\operatorname{Aut}(H_n)|\) and \(a_n=\log h_n\). Components arising from different indices \(j\) are nonisomorphic, while the \(\binom{n}{j}\) identical copies for a fixed \(j\) may be permuted. Therefore
\[
h_n=\prod_{j=0}^{n-1}\binom{n}{j}!\;h_j^{\binom{n}{j}},
\]
so, with \(f_n\) as above,
\[
a_n=f_n+\sum_{j=0}^{n-1}\binom{n}{j}a_j.
\]
Set
\[
A(z)=\sum_{n\ge0}a_n\frac{z^n}{n!}.
\]
The exponential generating function of the binomial transform is \(e^zA(z)\). Adding the omitted \(j=n\) term to the recurrence gives
\[
2A(z)=e^zA(z)+\Phi(z),
\]
hence
\[
A(z)=\frac{\Phi(z)}{2-e^z}.
\]
Moreover,
\[
0\le f_n\le n(\log 2)2^n,
\]
because \(\log(\binom{n}{j}!)\le \binom{n}{j}\log\binom{n}{j}\le n(\log2)\binom{n}{j}\). Thus \(\Phi\) is entire.

The poles of \(A\) can only occur at \(L+2\pi i k\), where \(k\in\mathbb Z\). The unique pole of smallest modulus is the simple pole at \(z=L\), and
\[
A(z)=\frac{\Phi(L)}{2L}\frac{1}{1-z/L}+B(z),
\]
where \(B\) is analytic in every closed disk of radius \(R<\sqrt{L^2+4\pi^2}\). Cauchy's coefficient estimate therefore yields
\[
a_n=\frac{\kappa}{2}\frac{n!}{L^{n+1}}+O\!\left(n!R^{-n}\right).
\]
Finally, the published isomorphism \(\operatorname{Aut}(G_n)\cong\operatorname{Aut}(H_n)^2\) doubles the logarithm and proves the displayed asymptotic.

## Verification
The accompanying script independently evaluates the exact finite recurrence through \(n=4\), checks \(h_0,h_1,h_2,h_3=(1,1,2,288)\) and \(h_4=182601737180282880\), evaluates \(\kappa\) from seventy terms, and checks numerical convergence of \(L^{n+1}\log|\operatorname{Aut}(G_n)|/n!\) through \(n=12\). Its captured output ends with `VERIFY_OK`. This is a reproducibility check, not an independent audit or formal proof.

## Relationship to prior work
Aguzzoli, Gerla, and Marra's 2007 conference abstract, later developed in their 2008 paper, gives the path/forest dual description of Gödel algebras free over finite distributive lattices. Aguzzoli's 2020 paper gives the recursive forests \(H_n\), the exact automorphism-group decomposition, and exact finite formulas. The result here does not claim those finite formulas as new; it extracts their dominant analytic singularity and obtains the explicit sharp first-order asymptotic and normalized limit. Carai's 2026 generalization treats free algebras and coproducts in arbitrary varieties of Gödel algebras but does not state this automorphism-order asymptotic.

## Limitations
Novelty is best-of-knowledge rather than independently certified. The theorem concerns the ordinary finite automorphism group of each finitely generated free Gödel algebra and does not address endomorphism counts, infinite-generator automorphism groups, bounded-depth subvarieties, or refined distributional information inside the automorphism group. The numerical decimal for \(\kappa\) is supplementary; the exact constant is the convergent series \(\Phi(\log2)\).

## References
1. S. Aguzzoli, B. Gerla, V. Marra, “Gödel algebras free over finite distributive lattices,” TANCL 2007, Oxford, August 5–9, 2007; journal version, *Annals of Pure and Applied Logic* 155 (2008), 183–193, DOI 10.1016/j.apal.2008.04.003.
2. S. Aguzzoli, “Automorphism groups of Lindenbaum algebras of some propositional many-valued logics with locally finite algebraic semantics,” FUZZ-IEEE 2020, DOI 10.1109/FUZZ48607.2020.9177714.
3. L. Carai, “Free algebras and coproducts in varieties of Gödel algebras,” *Journal of Symbolic Logic* (2026), DOI 10.1017/jsl.2026.10194.
