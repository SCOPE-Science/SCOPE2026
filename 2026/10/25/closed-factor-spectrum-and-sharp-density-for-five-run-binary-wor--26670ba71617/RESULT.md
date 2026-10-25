# Closed-factor spectrum and sharp density for five-run binary words

## Finding

For all positive integers \(a,b,c,d,e\), put
\[w=0^a1^b0^c1^d0^e,\qquad n=a+b+c+d+e.\]
Let \(C_+(w)\) count the **distinct nonempty contiguous closed factors** of \(w\). Define
\[
\begin{aligned}
x&=\min(a,c),& y&=\min(c,e),&z&=\min(a,c,e),\\
t&=\min(b,d),& h&=\max(a,c,e),&j&=\max(b,d),\\
I&=\mathbf1_{b=d},&r&=\max(0,\min(a,e)-c).
\end{aligned}
\]
Then the exact five-parameter count is
\[\boxed{C_+(w)=h+j+x+y-Iz+t+t(x+y)+Ixy+r.}\]

If \(M_5(n)\) is the maximum of \(C_+(w)\) over all binary length-\(n\) words with exactly five maximal constant runs, then, as \(n\to\infty\),
\[\boxed{M_5(n)=\frac{n^2}{8}+O(n).}\]
For every \(k\ge1\), the explicit family
\[w_k=0^{2k}1^k0^{2k}1^k0^{2k}\]
has \(n=8k\) and \(C_+(w_k)=8k^2+6k\). Moreover, a sequence of five-run words with lengths \(n\to\infty\) satisfies \(C_+(w)=n^2/8+o(n^2)\) **if and only if**, after exchanging the symbols if necessary, it eventually has \(b=d\) and
\[\frac{(a,b,c,d,e)}n\longrightarrow
\left(\frac14,\frac18,\frac14,\frac18,\frac14\right).\]
Reversal gives the same limiting proportions. Thus the leading-density extremizer is rigid.

## Assumptions and scope

A factor is a contiguous substring, counted once regardless of multiplicity. A word of length one is closed. A word of length at least two is closed if some nonempty proper border occurs precisely twice, as its prefix and suffix; overlaps of these occurrences are permitted. This agrees with the complete-first-return definition. The empty word is **excluded** from \(C_+\); including it adds one to every displayed exact count. Each of the five run lengths is a strictly positive integer; every binary word with five runs begins either with \(0\) (the displayed form) or with \(1\) (obtained by symbol exchange). No properties of scattered subsequences are used.

## Proof

**Complete classification.** Every factor has between one and five runs. A one-run factor is closed, and its distinct possibilities are the \(h\) zero powers and \(j\) one powers. A two-run factor has no nonempty border and is open.

A three-run factor with outer letter \(0\) has the form \(0^i1^B0^j\) and is closed exactly when \(i=j\): its only possible border is a zero power, and unequal outer lengths yield additional occurrences inside the longer outer run. The only possible middle lengths are \(B=b,d\). Consequently these closed factors number \(x+y-Iz\); equal middle lengths cause exactly \(z\) duplicates. The three-run factors with outer letter \(1\) have middle run \(0^c\) and number \(t\).

A four-run factor starting with \(0\) has form \(0^i1^b0^c1^j\), with \(1\le i\le a\) and \(1\le j\le d\). Every nonempty border necessarily contains both symbols. For a prefix and suffix to agree, the prefix \(0^i1^j\) must fit before the first two-run boundary and after the second; this holds precisely when \(i\le c\) and \(j\le b\). The border occurs exactly twice, once across each \(01\) boundary. There are therefore \(xt\) such closed factors. Complementing/reversing the argument for the four-run factors starting with \(1\) gives \(ty\) factors of form \(1^i0^c1^d0^j\). The two collections have different initial symbols and cannot overlap.

Every five-run factor has the unique form \(0^i1^b0^c1^d0^j\) with \(1\le i\le a\), \(1\le j\le e\). A border consisting only of zeros can occur exactly twice if and only if \(i=j>c\), contributing \(r\) distinct factors. If the border contains a \(1\), it must contain one complete one-run in each occurrence, so \(b=d\); equality of the border on the two sides forces \(i\le c\) and \(j\le c\). Conversely, these conditions supply the border \(0^i1^b0^j\), appearing exactly once at each of the two one-runs, so the factor is closed. Such factors number \(Ixy\). The two five-run subfamilies are disjoint because the latter has \(i,j\le c\) and the former has \(i=j>c\).

Summing the mutually distinct families with one, three, four, and five runs yields the boxed exact formula. All necessity statements follow from where an occurrence of a border can begin and end; no other transition pattern is available in at most five runs.

**Sharp asymptotics.** Write the exact count as \(C_+(w)=Q+L\), where
\[Q=t(x+y)+Ixy\]
is its quadratic contribution. Every other term satisfies \(L=O(n)\), uniformly over positive run lengths. Put \(u=x+y\). The three zero runs obey
\[a+c+e\ge x+y+\max(x,y)\ge\tfrac32u,\]
and the two one runs obey \(b+d\ge2t\).

If \(b\ne d\), then \(I=0\), and optimization of \(tu\) under \(\tfrac32u+2t\le n\) gives
\[Q\le\frac{n^2}{12}.\]

If \(b=d=t\), let \(S=n-\tfrac32u-2t\ge0\). Since \(xy=(u^2-(x-y)^2)/4\), direct substitution yields the nonnegative defect identity
\[\frac{n^2}{8}-Q=
\frac12\left(u-\frac n2\right)^2+\frac14(x-y)^2+\frac12Su.\]
In particular \(Q\le n^2/8\) for both cases. Taking \((a,b,c,d,e)=(2k,k,2k,k,2k)\) proves the exact witness count \(8k^2+6k\); for arbitrary large \(n\), rounding the five prescribed proportions with total sum \(n\) gives \(n^2/8+O(n)\). Hence \(M_5(n)=n^2/8+O(n)\).

For rigidity, any asymptotically maximizing sequence has \(Q=n^2/8+o(n^2)\). The strict \(n^2/12\) bound rules out \(b\ne d\) eventually. The displayed defect identity then forces \(u=n/2+o(n)\), \(x-y=o(n)\), and \(S=o(n)\). Consequently \(x=y=n/4+o(n)\) and \(t=n/8+o(n)\). Since \(a\ge x\), \(e\ge y\), \(c\ge\max(x,y)\), and the nonnegative excesses add to \(S+o(n)\), all three zero-run lengths equal \(n/4+o(n)\). Conversely, these proportions and eventual \(b=d\) make \(Q=n^2/8+o(n^2)\), proving the equivalence.

## Verification

The bundled `verify.py` uses two independently specified finite procedures: direct substring enumeration with a border-occurrence test, and an explicit generation of exactly the factor families classified in the proof. Their full sets and their cardinalities agree for all \(5^5=3125\) positive run-length tuples with each coordinate at most five. The verifier additionally checks the exact witness formula for 500 values of \(k\) and computes the five-run maxima for lengths five through fourteen. Run with Python 3 using `python verify.py`; no third-party packages or external data are needed. These finite checks are not used as an infinite proof.

## Relationship to prior work

Badkobeh, Fici, and Lipták [1] introduced structural and extremal bounds for closed factors and gave a five-run quadratic-richness construction (Theorem 25). Parshina and Puzynina [2] proved the unrestricted asymptotic maximum \(n^2/6\), and their Example 1 highlights the family \(0^k1\,0^k1\,0^k\). Both previously studied constructions fall within the displayed five-run family, but their theorems do not state the full five-parameter classification, its sharp restricted leading coefficient \(1/8\), or the rigidity of near-extremizers. The general bound \(n^2/6\) is not sharp for the present restricted family.

## Limitations

The theorem concerns **exactly five nonempty maximal runs**, not an unrestricted word or a general alphabet. It provides the leading sharp maximum with an \(O(n)\) error but does not give an exact formula for \(M_5(n)\) at every finite length. The factor classification, by contrast, is exact for every five-tuple. A check of available literature and records did not identify a published equivalent; an unindexed special-case enumeration or an unpublished derivation remains possible. No independent validation has been performed.

## References

[1] G. Badkobeh, G. Fici, and Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395, initial public version May 2013 (revised December 2014); Theorem 25 and pages 2–4, 8–9. https://arxiv.org/abs/1305.6395

[2] O. Parshina and S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863, first public version November 1, 2021; Example 1, Theorem 3, Proposition 8, and concluding discussion. https://arxiv.org/abs/2111.00863
