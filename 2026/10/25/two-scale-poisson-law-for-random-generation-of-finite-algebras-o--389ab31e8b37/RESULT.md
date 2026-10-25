# Two-scale Poisson law for random generation of finite algebras of disjoint alternatives

## Finding

Consider the variety of algebras of disjoint alternatives (ADAs) in the signature without a designated undefined constant. The finite-pair representation of Ledda, Graziani and Vergottini implies that every nontrivial finite ADA is isomorphic to
\[ A_{r,s}=\mathbf 2^{r}\times\mathbf 3^{s},\qquad r,s\ge0,\quad r+s\ge1,\]
where \(\mathbf 2=\{F,T\}\) is the two-element subalgebra and \(\mathbf 3=\{F,U,T\}\) the three-element ADA. Distinct coordinates are labelled. For \(k\ge0\), the exact number of ordered generating \(k\)-tuples is
\[
 G_k(r,s)=(2^k)_{\underline r}\,(3^k-2^k)_{\underline s},
\]
where \((m)_{\underline j}=m(m-1)\cdots(m-j+1)\) for \(j\ge1\), \((m)_{\underline0}=1\), and the factorial is zero for \(j>m\). Hence the minimal generating rank is the least \(k\ge0\) with \(r\le2^k\) and \(s\le3^k-2^k\). If the \(k\) generators are chosen independently uniformly from \(A_{r,s}\), their generation probability is
\[
 p_k(r,s)=\frac{(2^k)_{\underline r}}{(2^k)^r}\,
             \frac{(3^k-2^k)_{\underline s}}{(3^k)^s}.
\]
For sequences \(k\to\infty\) and \(r=r_k,s=s_k\) satisfying \(r_k/2^{k/2}\to a\) and \(s_k/(3/2)^k\to b\), with finite \(a,b\ge0\), the binary collision count and the count of ternary coordinates receiving no undefined value converge **jointly to independent Poisson variables** with means \(a^2/2\) and \(b\), respectively. In particular,
\[
 \boxed{\lim_{k\to\infty} p_k(r_k,s_k)=\exp(-a^2/2-b).}
\]
More generally, as \(k\to\infty\), the probability tends to one if \(r_k^2/2^k+s_k(2/3)^k\to0\), and tends to zero if this quantity tends to infinity. The ternary birthday-collision probability disappears in the nontrivial two-scale window; the second Poisson obstruction is the absence of undefinedness, not ternary collisions.

## Assumptions and scope

The signature is \((\otimes,\oplus,\neg,\downarrow,0,1)\), with no distinguished constant \(U\). In \(\mathbf3\), \(F,U,T\) are respectively false, undefined and true; \(\neg F=T\), \(\neg U=U\), \(\neg T=F\), and \(\downarrow x=T\) exactly when \(x=T\), otherwise \(\downarrow x=F\). The left-sequential operations obey: \(x\otimes y\) equals \(F\) if \(x=F\), equals \(U\) if \(x=U\), and equals \(y\) if \(x=T\); \(x\oplus y\) equals \(T\) if \(x=T\), equals \(U\) if \(x=U\), and equals \(y\) if \(x=F\). All product operations act coordinatewise. The only probabilistic assumption is that each generator is uniform on the whole product, independently of the others. This is *not* Manes' stronger signature with a named undefined constant.

## Proof

**1. Product normal form.** For a finite Boolean algebra \(B\cong\mathcal P([r+s])\), every filter has the form \(F_B=\{X:C\subseteq X\}\) for some subset \(C\) of atoms. The pair representation \((B,F_B)\) consists of pairs \(x\le y\) obeying \(x\vee\neg y\in F_B\). At an atom in \(C\), the combination \((x,y)=(0,1)\) is excluded, leaving \(\mathbf2\); at atoms outside \(C\), all three pairs are allowed, yielding \(\mathbf3\). Thus every nontrivial finite ADA in this signature has the asserted product form. This conclusion uses the representation theorem of Ledda--Graziani--Vergottini; the stochastic statements below are not asserted in that source.

**2. Necessity of separation and definedness.** Given generators \(g_1,\ldots,g_k\), associate to each coordinate its word of their values. Two binary coordinates with the same word have identical evaluations under every term, so cannot be separated; the same is true for two ternary coordinates. A ternary coordinate whose word contains no \(U\) stays in \(\{F,T\}\) under every term and so cannot generate its own \(U\). The three requirements in the theorem are therefore necessary: binary words all distinct; ternary words all distinct; each ternary word contains \(U\). Such ternary words automatically differ from every binary word.

**3. Sufficiency using explicit selectors.** For a fixed input variable \(x_i\), the terms \(\downarrow x_i\), \(\downarrow\neg x_i\), and \(\neg(\downarrow x_i\oplus\downarrow\neg x_i)\) are crisp tests (outputs only \(F,T\)) for the respective values \(T,F,U\). Their sequential conjunction isolates any prescribed word in \(\{F,U,T\}^k\) on the finite list of coordinate words. All coordinate words are distinct under the stated requirements, so this constructs a crisp selector taking value \(T\) at exactly one coordinate. To assign \(U\) at a ternary coordinate, conjoin its selector on the left with an input \(g_i\) that equals \(U\) there; the result has \(U\) only at that coordinate. To assign \(T\) use its selector, and to assign \(F\) use zero. The sequential disjunction of these disjoint supported terms realizes every product element. The \(k=0\) case is checked directly: the sole nontrivial zero-generated product is \(\mathbf2\). This proves sufficiency.

**4. Exact counting.** There are \(2^k\) possible binary words, all admissible, and \(3^k-2^k\) admissible ternary words containing \(U\). Because the coordinates are labelled and the two sets of words are disjoint, injective assignments to the two coordinate groups are independent. This gives \(G_k\). There are \((2^r3^s)^k\) equally likely ordered generator tuples, so dividing gives \(p_k\).

**5. Joint Poisson law.** Put \(q=2^k\), \(u=3^k\). Let \(X\) count unordered equal pairs among the \(r\) independent binary words; let \(Y\) count ternary words with no \(U\), each independently with probability \(q/u=(2/3)^k\); and let \(Z\) count equal pairs among ternary words. Then \(X\) and \(Y\) are independent, \(\mathbb E X=\binom r2/q\to a^2/2\), and \(Y\sim\operatorname{Bin}(s,q/u)\Rightarrow\operatorname{Pois}(b)\). For \(X\), the usual factorial-moment proof of the birthday Poisson law applies: contributions from disjoint pairs give \((a^2/2)^j\), while any connected pattern of at least three vertices has order \(O(q^{1-v/2})=o(1)\) for its \(v\ge3\) vertices. Thus \(X\Rightarrow\operatorname{Pois}(a^2/2)\). Finally \(\mathbb E Z\le\binom s2/u=O((3/4)^k)\to0\), so \(\Pr(Z>0)\to0\). Generation occurs exactly on \(\{X=Y=Z=0\}\), yielding the limit.

**6. Sharp outer regimes.** When \(r^2/q+s(q/u)\to0\), the union bound controls binary collisions and missing-\(U\) words. Moreover \(s^2/u=(s q/u)^2(u/q^2)\). Since \(u/q^2=(3/4)^k\to0\), ternary collisions vanish as well. For the zero regime, \(p_k\le\exp[-r(r-1)/(2q)]\) and \(p_k\le\exp[-s(q/u)]\); if \(r^2/q+s(q/u)\to\infty\), their maximum tends to infinity. This proves the two threshold alternatives.

## Verification

The accompanying standalone `checker.py` independently implements all primitive operations and the closure under terms. It exhaustively enumerates ordered generating tuples on twelve small \((r,s,k)\) parameter instances, including mixed Boolean/ternary cases and the zero-generator case, then checks the resulting counts against the falling-factorial expression. The command `python checker.py` prints `ALL_CHECKS_OK` on success. This finite diagnostic is **not** a substitute for the proof of the infinite-parameter classification or Poisson limit.

## Relationship to prior work

Ledda, Graziani and Vergottini (2026, DOI below), Theorem 7 and its finite Boolean-filter specialization, provide the product representation. No random generation probability or two-scale limit was observed in its extensive indexed passages, which included its stated contributions and conclusions. Sipoş (first publicly posted 2023, Theorem 2.4) gives a disjunctive normal form for term functions on Łukasiewicz--Moisil algebras, making the deterministic separation criterion an accessible consequence of earlier general theory. The exact falling-factorial enumeration is presented here as the elementary bridge to, **not independently as priority over**, that normal-form framework. The assessed additional result is the joint, independent Poisson limit and its competition between two distinct obstruction mechanisms in uniformly random generating tuples.

## Limitations

The random choices are independent uniform elements of labelled finite products. Nonuniform, dependent, infinite, or pointed ADA signatures are outside scope. These asymptotics are for sequences with \(k\to\infty\); they do not claim uniform finite-size error bounds. The exact rank formula is not asserted as an independently novel consequence of the older normal-form literature. A broad historical priority claim beyond the inspected sources is not made.

## References

1. A. Ledda, P. Graziani and A. Vergottini, *A Common External Framework for Kleene and McCarthy Algebras*, *Mathematical Logic Quarterly*, first published 2026-09-24, DOI 10.1002/malq.70026; especially Theorems 6 and 7 and Corollary 1.
2. A. Sipoş, *Normal forms and representable functions in Moisil logic*, arXiv:2304.00288, first posted 2023-04-01; *Algebra Universalis* 87 (2026), article 10, DOI 10.1007/s00012-026-00924-z; especially Theorem 2.4.
