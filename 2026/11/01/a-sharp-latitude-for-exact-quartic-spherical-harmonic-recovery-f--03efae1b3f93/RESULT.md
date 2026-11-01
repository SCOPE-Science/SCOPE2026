# A sharp latitude for exact quartic spherical-harmonic recovery from one regular polygon

## Finding

For every integer \(N\ge9\), place \(N\) equally spaced samples on a circle of constant height \(z\in[-1,1]\) on \(S^2\). Restrict the nine-dimensional space \(\mathcal H_4(S^2)\) of **exact-degree-four** spherical harmonics to these samples, using equal sample weights and an orthonormal harmonic basis for probability area measure. Write \(t=z^2\), and denote the evaluation matrix by \(E_{N,z}\). Its nine Gram eigenvalues, counted with multiplicity, are

\[
9N\{a_0(t)\ [1],\ a_1(t)\ [2],\ a_2(t)\ [2],\ a_3(t)\ [2],\ a_4(t)\ [2]\},
\]

where

\[
\begin{aligned}
a_0(t)&=\frac{(35t^2-30t+3)^2}{64},\\
a_1(t)&=\frac{5}{16}t(1-t)(7t-3)^2,\\
a_2(t)&=\frac{5}{32}(1-t)^2(7t-1)^2,\\
a_3(t)&=\frac{35}{16}t(1-t)^3,\\
a_4(t)&=\frac{35}{128}(1-t)^4.
\end{aligned}
\]

The spectrum is independent of the initial longitude, and \(a_0+2(a_1+a_2+a_3+a_4)=1\). At full-rank heights define \(\kappa_2(E_{N,z})\) as the spectral condition number, and set it to \(+\infty\) at rank-deficient heights. The sharp global optimum, independent of \(N\ge9\), is

\[
\boxed{\min_{-1\le z\le1}\kappa_2(E_{N,z})^2
=\frac{7(1-\tau)^2}{(7\tau-3)^2}
=3.218558589055428109\ldots,}
\]

where \(\tau=0.276050899448067155\ldots\) is the **unique** root in \((1/4,1/3)\) of

\[
147\tau^3-147\tau^2+33\tau-1=0.
\]

Equality holds exactly at the two heights \(z=\pm\sqrt\tau\), at every choice of initial longitude. Thus the minimum ordinary condition number is \(1.794034166078067786\ldots\). At either optimum, \(a_1=a_2\) is the least eigenvalue level and \(a_3\) is the largest; hence the smallest Gram eigenvalue has multiplicity four, and the largest has multiplicity two.

## Assumptions and scope

Let \(x_j=(\sqrt{1-z^2}\cos(\phi_0+2\pi j/N),\sqrt{1-z^2}\sin(\phi_0+2\pi j/N),z)\), for \(0\le j<N\), with arbitrary \(\phi_0\in\mathbb R\). Each evaluation row corresponds to one such point. The domain is precisely \(\mathcal H_4(S^2)\), not the space of harmonics of degree at most four. Let the surface area probability measure be \(\mathrm d\sigma/(4\pi)\); then the usual complex spherical harmonics are multiplied by \(\sqrt{4\pi}\) to become orthonormal for this measure. The Gram matrix is \(E_{N,z}^*E_{N,z}\) without row rescaling. Only its global scalar changes if the standard area normalization is used instead. In particular, the condition-number assertion is unaffected.

The requirement \(N\ge9\) guarantees distinct angular frequencies \(-4,-3,\ldots,4\) modulo \(N\). Nine samples are the minimum possible sample count for injective evaluation on this nine-dimensional space, and the theorem covers every greater regular-polygon sample count. It makes no claim of optimality among irregular point sets, multiple-latitude configurations, or reconstructions of arbitrary degree-at-most-four signals.

## Proof

**1. Exact Gram spectrum.** Set \(P_4(s)=(35s^4-30s^2+3)/8\), and for \(0\le j\le4\) take the associated Legendre form

\[
P_4^j(s)=(-1)^j(1-s^2)^{j/2}\frac{\mathrm d^j}{\mathrm ds^j}P_4(s).
\]

The usual normalized spherical harmonic of azimuthal order \(j\) has squared latitude amplitude

\[
9\,\frac{(4-j)!}{(4+j)!}\bigl(P_4^j(z)\bigr)^2=9a_j(t).
\]

The negative azimuthal orders have the same squared amplitudes. Since \(N\ge9\), discrete Fourier orthogonality \(\sum_{q=0}^{N-1}e^{2\pi i(q/N)(j-k)}=N\mathbf1_{\{j=k\}}\), for \(-4\le j,k\le4\), makes the harmonic Gram diagonal. Its entries are \(9N a_{|j|}(t)\). Differentiating \(P_4\) yields the five stated explicit polynomials. Their weighted sum is identically one, as also follows from the harmonic addition theorem. An initial-longitude rotation multiplies columns by unimodular phases and therefore leaves the spectrum unchanged.

**2. Reduction to a sharp one-dimensional minimax problem.** For all \(t\in[0,1]\), set

\[
R(t)=\frac{\max_{0\le j\le4}a_j(t)}{\min_{0\le j\le4}a_j(t)},
\]

with \(R(t)=+\infty\) when any \(a_j(t)=0\). Exact polynomial certificates show

\[
R(t)\ge \frac{13}{4}\quad\text{on}\quad
[0,1/4]\cup[1/3,1].
\]

For completeness, the following five nonnegative polynomial inequalities cover this entire outer set; the indicated symbols refer to the functions above:

| Closed interval for \(t\) | Polynomial certified nonnegative |
| --- | --- |
| \([0,3/100]\) | \(4a_4-13a_3\) |
| \([3/100,3/20]\) | \(4a_4-13a_0\) |
| \([3/20,1/4]\) | \(4a_3-13a_2\) |
| \([1/3,1/2]\) | \(4a_3-13a_1\) |
| \([1/2,1]\) | \(4a_2-13a_4\) |

Each is verified **exactly** by its degree-four Bernstein representation after mapping the respective interval affinely to \([0,1]\): every Bernstein coefficient is nonnegative. The complete rational coefficient lists are printed by the embedded standard-library program `CHECK.py`, and are checked afresh during its execution. A nonnegative Bernstein combination on \([0,1]\) establishes the inequality on the whole interval; no point sampling or numerical root guessing is used in this step.

**3. Interior minimax and equality.** The factorization

\[
a_1(t)-a_2(t)=\frac5{32}(1-t)\,p(t),\qquad
p(t)=147t^3-147t^2+33t-1
\]

has a unique root \(\tau\in(1/4,1/3)\), because \(p\) is strictly decreasing there and has opposite endpoint signs. More precisely, \(p''(t)=882t-294\le0\) there and \(p'(1/4)<0\). For \(1/4\le t\le\tau\), \(a_2\le a_1\), and

\[
R(t)\ge\frac{a_3(t)}{a_2(t)}
=\frac{14t(1-t)}{(7t-1)^2}.
\]

Its derivative is \(-14(5t+1)/(7t-1)^3<0\) throughout that interval. For \(\tau\le t\le1/3\), \(a_1\le a_2\), and

\[
R(t)\ge\frac{a_3(t)}{a_1(t)}
=\frac{7(1-t)^2}{(7t-3)^2}.
\]

Its derivative is \(56(t-1)/(7t-3)^3>0\) throughout that interval. Both lower bounds meet at the common value \(C=7(1-\tau)^2/(7\tau-3)^2\). The exact isolating interval \(27605/100000<\tau<27606/100000\) proves \(C<13/4\); therefore no outer height can be optimal. Rational interval arithmetic on this same isolator shows \(a_3(\tau)>a_0(\tau),a_4(\tau)\) and \(a_0(\tau),a_4(\tau)>a_1(\tau)=a_2(\tau)\). Hence \(R(\tau)=C\). The strict monotonicities give uniqueness of the squared optimal height, completing the proof.

## Verification

`CHECK.py` is a standalone Python 3 standard-library checker. It constructs the five polynomials with rational arithmetic; verifies the weighted addition-theorem identity, the five complete Bernstein certificates, an exact cubic-root isolator and rational ordering inequalities at the optimum; and independently constructs Gram matrices from associated Legendre derivatives at several positive heights. The direct complex Gram tests cover \(N\in\{9,10,13\}\) and five heights each, checking \(1215\) matrix entries. All tests passed when executed from the actual embedded checker. The finite Gram calculations corroborate the separate all-height proof; they are not offered as its replacement.

## Relationship to prior work

Bannai, Okuda and Tagami (2013) construct harmonic-index designs by lifting regular polygons to roots of Gegenbauer polynomials; this gives a moment-cancellation property at special latitudes, **not** the full-rank singular-value minimax problem here. Their source includes the regular-five-gon harmonic-index-four construction, a distinct sampling objective. Zhu and collaborators (2015) extend the theory and classification of harmonic-index designs, not this condition-number optimization. Khalid, Kennedy and McEwen (2014) study stable iso-latitude transforms for **full degree-bounded spaces** using several rings and numerical ring placement; their matrices and optimization domains differ. Here a single ring supports an exact-degree-four nine-dimensional space and admits a closed-form global algebraic minimizer, with an explicit rational certificate. The general associated-Legendre normalization and Fourier orthogonality are standard inputs, not asserted novelties.

## Limitations

Only exact degree four, equal weights, and one equally spaced latitude circle with \(N\ge9\) are covered. A nonregular configuration could have better conditioning, and no optimality among such configurations is claimed. The result is not a spherical cubature theorem or a stability bound for all degrees up to four. The mathematical and literature comparison is bounded and not an independent external audit. An equivalent characterization in earlier specialized ring-sampling literature cannot be ruled out solely from indexed search results.

## References

1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101 (first public version 2013-08-23), especially Theorem 1 and its proof. https://arxiv.org/abs/1308.5101
2. Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661 (first public version 2014-03-19), especially Sections II–III and latitude conditioning discussion. https://arxiv.org/abs/1403.4661
3. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373 (first public version 2015-07-20), especially Sections 1–3. https://arxiv.org/abs/1507.05373
