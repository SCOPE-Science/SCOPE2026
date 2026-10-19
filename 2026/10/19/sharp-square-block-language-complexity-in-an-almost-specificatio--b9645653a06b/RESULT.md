# Sharp square-block language complexity in an almost-specification construction

## Finding

For integers \(p,q\ge2\), consider the colored-marker subshifts of Kwietniak, Oprocha, and Rams described below. Suppose the color restrictions at run length \(\ell\) comprise exactly \(\lfloor\sqrt\ell\rfloor\) coordinates and the explicitly defined renewal mass \(\rho=(1+p(3q-1)/(q-1)^2)/q\) is less than one. If \(b_n\) counts distinct admissible words of length \(n\), put \(k=\lfloor\sqrt{n-1}\rfloor\) and \(s=n-1-k^2\). Then, as \(n\to\infty\),

\[
\frac p{1-\rho}-\frac{b_n}{q^n}
\sim
\frac{p^2}{q(1-\rho)^2}\,q^{-k}
\left(2k+1-s+\frac{2k+1}{q-1}+\frac{2q}{(q-1)^2}\right).
\]

For the original parameter choice \(p=2,q=4\), this becomes the explicit *square-block phase law*

\[
\boxed{\frac{72}{5}-\frac{b_n}{4^n}\sim
\frac{1296}{25}\,4^{-k}\left(\frac{8k}{3}-s+\frac{20}{9}\right).}
\]

If \(s/(2k)\to t\in[0,1]\), the scaled deficit divided by \(k4^{-k}\) converges to \((1296/25)(8/3-2t)\). Its complete set of subsequential limits is the nontrivial interval \([864/25,3456/25]\). Thus a *single* stretched-exponential approximation with a constant leading prefactor does not describe the discrepancy at its natural square-block scale.

The exact \(b_n\), not just this asymptotic, depends **only** on \(\lfloor\sqrt\ell\rfloor\), not on the permitted coordinate locations. In particular, the two canonical choices \(R_\ell=\{1,\ldots,\lfloor\sqrt\ell\rfloor\}\) and \(R_\ell=\{j^2:j^2\le\ell\}\) have identical length-by-length language complexity, although the motivating paper establishes different weak-specification behavior for these two choices. The weak-specification distinction itself is prior work.

## Assumptions and scope

Let the alphabet consist of a marker \(0\), and \(pq\) nonmarker symbols \((a,b)\), where \(a\in\{1,\ldots,p\}\) is a color and \(b\in\{0,\ldots,q-1\}\) is a digit. At each integer length \(\ell\ge1\), choose nested coordinate sets \(R_\ell\subseteq\{1,\ldots,\ell\}\) with \(|R_\ell|=\lfloor\sqrt\ell\rfloor\). A restricted word of length \(\ell\) is monochromatic in \(a\), and has digit \(b=0\) at every position in \(R_\ell\). A *free word* is one marker followed by a restricted word, allowing the restricted suffix to have length zero. A *good word* is a finite concatenation of free words, including the empty concatenation. The construction's language consists of all words obtained from an unrestricted monochromatic nonmarker prefix (possibly empty) followed by a good word. Its shift space is the corresponding closed subshift.

Let \(f_m\) count free words of length \(m\), let \(G_m\) count good words of length \(m\), with \(G_0=1\), and let \(b_n\) count the full language's length-\(n\) words. The result concerns word complexity, not the number of periodic points, an invariant measure's cylinder probabilities, or a rate of specification.

## Proof

**1. Exact combinatorial renewal.** The marker yields an unambiguous decomposition of every nonempty good word into its first free word followed by another good word. Hence

\[
f_1=1,\qquad f_m=pq^{m-1-\lfloor\sqrt{m-1}\rfloor}\ (m\ge2),
\qquad G_n=\sum_{m=1}^n f_m G_{n-m}.
\]

Every full-language word either contains no marker (there are \(pq^n\) such words), begins with a marker (there are \(G_n\) such words), or first meets a marker after a uniquely determined nonempty monochromatic prefix. Therefore the exact, overlap-free identity is

\[
b_n=pq^n+G_n+p\sum_{j=1}^{n-1}q^{n-j}G_j.
\]

The formulas depend on \(R_\ell\) only through \(|R_\ell|\). Consequently, different nested restriction sets of the specified cardinalities yield the same \(b_n\), for every \(n\ge1\).

**2. The subcritical normalization.** Set \(a_m=f_m/q^m\), \(g_m=G_m/q^m\). Then \(g_0=1\) and \(g_m=\sum_{j=1}^m a_jg_{m-j}\). Since there are \(2k+1\) positive integers \(\ell\) in the interval \(k^2\le\ell<(k+1)^2\),

\[
\sum_{\ell\ge1}q^{-\lfloor\sqrt\ell\rfloor}
=\sum_{k\ge1}(2k+1)q^{-k}
=\frac{3q-1}{(q-1)^2}.
\]

Thus \(\rho:=\sum_{m\ge1}a_m=[1+p(3q-1)/(q-1)^2]/q<1\). With \(\delta:=1-\rho>0\), summing the absolutely convergent renewal series gives \(\sum_{m\ge0}g_m=1/\delta\). Dividing the exact language formula by \(q^n\) yields

\[
\frac{b_n}{q^n}=p\sum_{m=0}^{n-1}g_m+g_n.
\]

In particular, the limit is \(p/\delta\) and its *signed* deficit is

\[
\Delta_n:=\frac p\delta-\frac{b_n}{q^n}
=p\sum_{m\ge n}g_m-g_n.
\]

The quantity is eventually positive by the asymptotics proved below.

**3. An exactly summable square-block tail.** For \(n\ge2\), put \(k=\lfloor\sqrt{n-1}\rfloor\) and \(s=n-1-k^2\), so \(0\le s\le2k\). Summing the remainder of the current square block and the complete subsequent blocks yields the exact identity

\[
A_n:=\sum_{m\ge n}a_m
=\frac pq\,q^{-k}\left(2k+1-s+\frac{2k+1}{q-1}
+\frac{2q}{(q-1)^2}\right).
\]

It follows uniformly over the square-block phase that \(A_n\asymp\sqrt n\,q^{-\sqrt n}\), while for every \(m\ge2\), \(a_m\) is between fixed positive multiples of \(q^{-\sqrt m}\). For \(h_n=\lfloor n^{1/3}\rfloor\), \(A_{n-h_n}/A_n\to1\), since at most \(h_n\) removed summands each have size \(O(q^{-\sqrt n})\), while \(A_n\gg\sqrt n\,q^{-\sqrt n}\).

**4. Subexponentiality and the geometric renewal tail.** Let \(X\) be a positive integer random variable with \(\Pr(X=m)=a_m/\rho\), and let \(X'\) be independent with the same law. The previous long-tail estimate provides the two contributions \(X\ge n-h_n\) and \(X'\ge n-h_n\) to the convolution tail. All other contributions have both summands at least \(h_n\), and the convolution bound

\[
\sum_{j=h_n}^{n-h_n} a_j A_{n-j}
\le C n^{3/2}\exp\{-\log(q)(\sqrt n+c\sqrt{h_n})\}=o(A_n)
\]

holds for a fixed \(c>0\), using \(\sqrt j+\sqrt{n-j}\ge\sqrt n+c\sqrt{h_n}\) on this central range. The intersection of the two large-summand contributions is \(O(A_{n-h_n}^2)=o(A_n)\). Together with the corresponding lower bound this proves

\[
\Pr(X+X'\ge n)\sim2\Pr(X\ge n),
\]

so the increment distribution is subexponential. Now let \(N\) be independent and geometric on \(\{0,1,\ldots\}\), with \(\Pr(N=r)=\delta\rho^r\). The law of \(X_1+\cdots+X_N\), including the empty sum, has mass \(\delta g_m\) at \(m\). The standard theorem for an independently and light-tailedly stopped sum of subexponential nonnegative increments gives

\[
\delta\sum_{m\ge n}g_m
\sim \mathbb EN\,\Pr(X\ge n)
=\frac\rho\delta\frac{A_n}{\rho},
\qquad\text{hence}\qquad
\sum_{m\ge n}g_m\sim\frac{A_n}{\delta^2}.
\]

This is precisely the classical randomly stopped-sum tail theorem; no new general renewal theorem is claimed here. Since \(A_{n+1}/A_n\to1\), the same renewal-tail equivalence at consecutive indices implies \(g_n=o(\sum_{m\ge n}g_m)\). Substitution into \(\Delta_n\) gives

\[
\Delta_n\sim\frac p{\delta^2}A_n,
\]

which, with the exact formula in step 3, proves the asserted word-complexity asymptotic.

**5. Phase and the concrete parameters.** For \(p=2,q=4\), \(\rho=31/36\), \(\delta=5/36\), and the exact tail simplifies to \(A_n=(1/2)4^{-k}((8/3)k-s+20/9)\). Thus \(pA_n/\delta^2=(1296/25)4^{-k}((8/3)k-s+20/9)\). As \(k\to\infty\), all values \(s/(2k)\to t\in[0,1]\) are realized by integers \(n=k^2+s+1\). The phase limits are therefore exactly the claimed interval, with distinct endpoints.

## Verification

The independent standard-library program `verify.py` exhaustively compares the exact recurrence against direct word enumeration through length five for both concrete restriction sets. It verifies twenty exact square-block tails using rational arithmetic and independently checks the subcritical mass, normalized limit and phase endpoint constants. Execute `python3 verify.py` with no external packages. These finite checks do not establish the infinite subexponential-renewal limit; steps 3–5 provide the mathematical argument for that limit.

## Relationship to prior work

Kwietniak, Oprocha, and Rams introduced this colored-marker shift construction, the free/good decomposition, its entropy considerations, and the contrasting weak-specification behavior of the two choices of restriction coordinates. Those contributions and the combinatorial renewal starting point are prior work. The present contribution is the explicit *sharp normalized language deficit*, including its nonconstant square-block phase envelope, coupled with the exact all-length indistinguishability of those two variants by language complexity. Pavlov's related almost-specification counterexamples are a distinct construction. The random-sum tail theorem applied in step 4 is standard and is credited to the heavy-tail renewal literature.

## Limitations

The leading deficit requires \(\rho<1\); no assertion is made at or above the renewal critical point. The phase law is an asymptotic equivalence with unusually slow possible numerical approach. The calculation does not yield a new specification theorem, establish new measure-theoretic uniqueness properties, or cover a different restriction-cardinality growth law. Even detailed literature comparison cannot rule out an earlier unindexed equivalent calculation. Independent scholarly priority and proof review have not been performed.

## References

1. D. Kwietniak, P. Oprocha, M. Rams, *On entropy of dynamical systems with almost specification*, arXiv:1411.1989v1 (first public 2014-11-07), Sections 4.1–4.6, https://arxiv.org/abs/1411.1989.
2. R. Pavlov, *On intrinsic ergodicity and weakenings of the specification property*, arXiv:1411.2077v1 (2014), https://arxiv.org/abs/1411.2077.
3. D. Denisov, S. Foss, D. Korshunov, *Asymptotics of randomly stopped sums in the presence of heavy tails*, Bernoulli 16 (2010), 971–994, arXiv:0808.3697, https://arxiv.org/abs/0808.3697.
