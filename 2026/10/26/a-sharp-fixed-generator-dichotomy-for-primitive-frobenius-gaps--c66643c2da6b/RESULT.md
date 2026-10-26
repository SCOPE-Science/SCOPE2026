# A sharp fixed-generator dichotomy for primitive Frobenius gaps

## Finding
For coprime positive integers \(a,b\), let \(g(a,b)\) be the largest nonnegative integer that has no representation \(n=ax+by\) with \(x,y\in\mathbb Z_{\ge0}\) and \(\gcd(x,y)=1\). This number is finite by the cited foundational theorem.

**Theorem.** For each fixed integer \(a\ge3\),
\[
\limsup_{\substack{b\to\infty\\b\equiv-1\pmod a}}
 \frac{g(a,b)}{b}=+\infty.
\]
More precisely, let \(L\ge2\) be an even integer and put
\[
N_{a,L}=\prod_{j=1}^L(aj-1),\qquad
b_{a,L}=\min\{b\ge1: b\equiv-1\pmod a,\ b>N_{a,L}/(aL)\}.
\]
Then \(\gcd(a,b_{a,L})=1\), the positive integer \(N_{a,L}\) has no primitive \((a,b_{a,L})\)-representation, and
\[
  g(a,b_{a,L})\ge N_{a,L},\qquad
  \frac{g(a,b_{a,L})}{b_{a,L}}
  \ge\frac{aL}{1+a^2L/N_{a,L}}\longrightarrow+\infty
  \quad(L\to\infty\text{ through even integers}).
\]
Together with the already-published formulas for \(a=1,2\), this makes \(a=3\) the sharp transition: the ratio \(g(a,b)/b\) stays uniformly bounded as admissible \(b\) varies exactly when the fixed positive generator \(a\) is \(1\) or \(2\).

## Assumptions and scope
The coefficients \(x,y\) may vanish, but must be nonnegative integers with gcd exactly \(1\); \(\gcd(0,k)=k\). The generators \(a,b\) are positive and coprime. The infinity statement fixes \(a\) and lets \(b\) vary over the explicitly constructed congruence class. It does not assert monotonicity of \(g(a,b)\) or quantify \(g\) at all \(b\).

## Proof
Fix \(a\ge3\) and an even \(L\ge2\). Set \(N=\prod_{j=1}^L(aj-1)\) and take \(b\) as in the theorem. Each factor of \(N\) is congruent to \(-1\pmod a\), hence \(N\equiv1\pmod a\). Also \(b\equiv-1\pmod a\), so \(\gcd(a,b)=1\).

Suppose for contradiction that \(N=ax+by\) with \(x,y\ge0\) and \(\gcd(x,y)=1\). Reduction modulo \(a\) gives \(y\equiv-1\pmod a\). Thus \(y=aj-1\) for some integer \(j\ge1\), and in particular \(y\ge a-1\ge2\). The inequality \(by\le N\) and the strict choice \(b>N/(aL)\) give \(y<N/b<aL\), hence \(j\le L\). Therefore \(y\) is a factor of \(N\), so \(y\mid N\). From \(ax=N-by\) we obtain \(y\mid ax\). Since \(\gcd(y,a)=1\), it follows that \(y\mid x\), and consequently \(\gcd(x,y)=y\ge2\), a contradiction. Thus \(g(a,b)\ge N\).

The least eligible \(b\) lies in an arithmetic progression of step \(a\), so \(b\le N/(aL)+a\). Consequently
\[
\frac{g(a,b)}b\ge\frac Nb\ge
\frac{N}{N/(aL)+a}=
\frac{aL}{1+a^2L/N}.
\]
For fixed \(a\ge3\), \(N\ge(a-1)^L\); thus \(N/(a^2L)\to\infty\), and the displayed lower bound diverges. Also \(b>N/(aL)\to\infty\), proving the limsup assertion.

For the boundary cases, Jaffe's Propositions 5.1–5.2 give \(g(1,b)=b-1\) except \(g(1,2)=0\), and \(g(2,b)=4b-2\) for odd \(b>1\). Hence for fixed \(a=1,2\) the ratio is bounded over admissible \(b\); for every \(a\ge3\) it is unbounded. This is the stated sharp dichotomy. \(\square\)

## Verification
The standalone `verify.py` uses only Python standard-library integer arithmetic. It constructs \(N_{a,L}\) and the least admissible \(b_{a,L}\), then independently enumerates every \((x,y)\ge0\) satisfying \(ax+by=N_{a,L}\) for \(3\le a\le13\) and even \(2\le L\le14\). It confirms that every such representation has gcd at least \(a-1\), and checks the exact lower bound by rational arithmetic. It reports 77 tested parameter pairs and 616 ordinary representations with no primitive instance. These checks are finite corroboration; the preceding divisibility proof establishes the full theorem.

Example: for \(a=3,L=4\), the construction gives \(N=880\) and \(b=74\). The admissible coefficients of \(b\) are \(2,5,8,11\), and all corresponding coefficients of \(a\) share the respective nontrivial factor.

## Relationship to prior work
Grace Natalie Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers* (arXiv:2610.17267v1, 12 October 2026) proves existence of \(g(a,b)\) (Theorem 4.3), establishes the primitive-representation characterization (Theorem 2.1), and gives exact formulas for \(a=1,2\) (Propositions 5.1–5.2). Its later sections explore upper bounds and parameter-dependent behavior. The present result concerns a different quantified phenomenon: for each fixed \(a\ge3\), no bound of the form \(g(a,b)\le C_a b\) can hold uniformly over admissible \(b\). None of those cited assertions supplies this dichotomy. The proof uses an explicit simultaneous divisibility obstruction, not a computed table of individual gaps.

## Limitations
This establishes a lower bound along a sparse explicit subsequence, not an asymptotic for all \(b\), nor a formula for the exact gap at those parameters. The novelty comparison is based on inspected primary literature and targeted searches, not exhaustive discovery of every potentially equivalent result; older treatments of restricted Frobenius problems might contain a stronger general statement.

## References
Jaffe, G. N. (2026). *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*. arXiv:2610.17267v1, https://arxiv.org/abs/2610.17267 . See Theorems 2.1, 4.3; Propositions 5.1, 5.2; §§6–7.
