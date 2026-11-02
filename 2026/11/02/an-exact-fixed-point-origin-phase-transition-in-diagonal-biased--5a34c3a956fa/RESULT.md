# An exact fixed-point–origin phase transition in diagonal-biased random mappings

## Finding

Let \(n\ge2\), and let \(T:[n]\to[n]\) have independent images satisfying \(\Pr(T(i)=i)=q\) and \(\Pr(T(i)=j)=(1-q)/(n-1)\) for \(j\ne i\), where \(0\le q\le1\). Write \(F=\#\{i:T(i)=i\}\) for the number of fixed points (loops), and \(L=\#\{j:T^{-1}(j)=\varnothing\}\) for the number of origins (zero-indegree vertices). Set \(r=(1-q)/(n-1)\).

**Complete joint law.** When \(0<q<1\), conditionally on \(F=f\), for each integer \(0\le s\le n-f\),
\[
\mathbb E[(L)_{\underline{s}}\mid F=f]
=(n-f)_{\underline{s}}
\left(\frac{n-s}{n-1}\right)^s
\left(\frac{n-s-1}{n-1}\right)^{n-f-s},
\]
with the convention \(0^0=1\). Consequently the complete joint probability-generating polynomial is
\[
\begin{aligned}
\mathbb E[t^F(1+z)^L]
={}&\sum_{f=0}^n\binom nf q^f(1-q)^{n-f}t^f\\
&\quad\cdot\sum_{s=0}^{n-f}\binom{n-f}s z^s
\left(\frac{n-s}{n-1}\right)^s
\left(\frac{n-s-1}{n-1}\right)^{n-f-s}.
\end{aligned}
\]
The polynomial identity extends to \(q=0,1\), where conditional claims about null events are not asserted.

**Exact sign transition.** For every \(n\ge2\) and \(0\le q\le1\),
\[
\operatorname{Cov}(F,L)
=\frac{nq(1-q)(1-q_\mathrm{off})^{n-2}(1-nq)}{n-1},
\qquad q_\mathrm{off}:=\frac{1-q}{n-1}.
\]
In particular, inside \(0<q<1\), the covariance is positive for \(q<1/n\), zero exactly at \(q=1/n\), and negative for \(q>1/n\). At the endpoints \(q=0,1\), one statistic is deterministic and covariance is zero.

**Nonmonotone regression and dependence at zero covariance.** For \(n\ge3\) and \(0<q<1\),
\[
\mathbb E[L\mid F=f]=(n-f)\left(\frac{n-2}{n-1}\right)^{n-f-1}
\quad(0\le f<n),\qquad \mathbb E[L\mid F=n]=0.
\]
The conditional expectation strictly rises from \(f=0\) to \(f=1\), has equal maxima at \(f=1\) and \(f=2\), and then strictly falls through \(f=n\). Therefore at the uniform-mapping point \(q=1/n\), \(F\) and \(L\) are uncorrelated but dependent.

## Assumptions and scope

The vertices are labeled, every map image is chosen independently, and diagonal versus off-diagonal target probabilities are exactly as specified. Origins count vertices of indegree zero (not vertices without ancestors). A loop is a one-cycle, not an arbitrary cyclic vertex. No limiting approximation or independence of \(F\) and \(L\) is assumed. The joint-factorial formula concerns possible values \(0\le f\le n\) for interior \(q\); when \(q\) is an endpoint only supported conditional events are meaningful.

## Proof

Because the choices \(\{T(i)\}\) are independent, \(F\sim\mathrm{Bin}(n,q)\). Fix exactly the loop set \(S\), of size \(f\); conditionally, each vertex outside \(S\) chooses independently and uniformly among its \(n-1\) other vertices, while a vertex in \(S\) maps to itself. Let \(R\subseteq[n]\setminus S\) have size \(s\). Every vertex of \(R\) can avoid sending an edge into \(R\) in exactly \(n-s\) of its \(n-1\) allowed destinations. Every vertex outside \(S\cup R\) can avoid \(R\) in exactly \(n-s-1\) of its \(n-1\) allowed destinations. Vertices of \(S\) automatically avoid \(R\). Thus the probability that every vertex of \(R\) is an origin is the product of the two fractions in the stated factorial formula. Summing over ordered \(s\)-tuples of distinct origins gives that formula. The binomial theorem \((1+z)^L=\sum_s(L)_{\underline{s}}z^s/s!\) and the binomial law of \(F\) give the complete joint polynomial.

For a single labeled vertex \(w\), \(\Pr(w\text{ is an origin})=(1-q)(1-r)^{n-1}\): the vertex does not map to itself, and the other \(n-1\) image choices each avoid it. For distinct \(v,w\), \(\Pr(T(v)=v,\ w\text{ is an origin})=q(1-q)(1-r)^{n-2}\). A loop cannot itself be an origin. Therefore
\[
\mathbb E[FL]=n(n-1)q(1-q)(1-r)^{n-2},\quad
\mathbb E F=nq,\quad
\mathbb E L=n(1-q)(1-r)^{n-1}.
\]
Subtracting products and using \((n-1)-n(1-r)=(1-nq)/(n-1)\) proves the covariance formula and strict interior signs.

Set \(c=(n-2)/(n-1)\), and define \(g(k)=kc^{k-1}\) for \(1\le k\le n\), with \(g(0)=0\). The conditional factorial formula at \(s=1\) says \(\mathbb E[L\mid F=f]=g(n-f)\). When \(n\ge3\),
\[
\frac{g(k+1)}{g(k)}=\frac{k+1}{k}\,\frac{n-2}{n-1}.
\]
This ratio is strictly greater than one for \(k<n-2\), equals one for \(k=n-2\), and is less than one for \(k>n-2\). The boundary \(g(0)=0<g(1)\) gives the stated regression sequence, including the equal maxima. At \(q=1/n\), every \(F=f\) has positive probability; its conditional expectation varies with \(f\), ruling out independence even though covariance vanishes.

## Verification

The included standalone Python program `verify.py` enumerates all \(n^n\) functions for \(2\le n\le5\), using exact rational probabilities at six values of \(q\) (with duplicates omitted). It compares the full joint table with the coefficient inversion of the joint generating polynomial, checks the exact covariance, and checks the conditional-regression shape through \(n=79\). It completed 742 exact assertions. These finite checks corroborate rather than replace the all-\(n\) proof above. Run `python verify.py` in a Python 3 environment; it uses only the standard library.

## Relationship to prior work

Independent-choice random mappings and the diagonal-biased family are explicitly described by Hansen and Jaworski's *A new random mapping model* (arXiv:math/0603529, first submitted 2006-03-22, introduction). Their paper develops mapping statistics, especially components and cyclic points; the stated joint fixed-point/origin factorial polynomial, covariance transition, and regression plateau are not among those inspected results. Arney and Bender (1982) develop origin-weighted generating functions and cycle statistics under indegree constraints, including the uniform family; their discussed joint origin/cycle framework does not itself determine the diagonal-biased loop–origin law. Hansen and Jaworski (2008) study an exchangeable-indegree model under a different conditional mapping construction. The original self-loop-biased mapping model also appears in Jaworski and Mutafchiev (1994), whose accessible abstract addresses largest-component behavior. These comparisons do not certify historical priority against every early local-statistics paper.

## Limitations

This result is exact for the independent-choice diagonal-biased model only; it does not claim the sign law for heterogeneous target matrices, fixed-indegree random mappings, or correlated image choices. Covariance zero does not assert independence. Historical priority remains uncertain because some earlier sources on local mapping structure and self-loop bias were accessible only as abstracts or bibliographic information. No independent mathematical audit has been performed.

## References

- J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529 (first public version 2006-03-22), https://arxiv.org/abs/math/0603529.
- J. C. Hansen and J. Jaworski, *Local properties of random mappings with exchangeable in-degrees*, Advances in Applied Probability 40 (2008), 183–205, https://doi.org/10.1239/aap/1208358892.
- J. Arney and E. A. Bender, *Random mappings with constraints on coalescence and number of origins*, Pacific Journal of Mathematics 103 (1982), 269–294, https://doi.org/10.2140/pjm.1982.103.269.
- J. Jaworski and L. Mutafchiev, *The largest connected component in a random mapping*, Random Structures & Algorithms 5 (1994), 73–94, https://doi.org/10.1002/rsa.3240050109.
