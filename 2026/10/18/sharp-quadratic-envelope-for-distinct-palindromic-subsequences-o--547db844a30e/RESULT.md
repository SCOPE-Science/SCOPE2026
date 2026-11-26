# Sharp extremal envelope and rigidity for scattered palindromes in binary words with three ones

## Finding

Let \(P(w)\) count distinct nonempty palindromic subsequence strings of \(w\). Write \(w=0^a1\,0^b1\,0^c1\,0^d\), where the gaps are nonnegative integers, and set \(z=a+b+c+d\). If \(M(z)\) is the maximum of \(P(w)\) over all these words with \(z\) zeros, then
\[
 M(z)=\frac{3}{16}z^2+O(z).
\]
In fact every such word satisfies \(P(w)\le 3z^2/16+3z+3\). Every sequence of maximizing gap quadruples, divided by \(z\), converges to \((1/4,1/4,1/4,1/4)\) as \(z\to\infty\). This is an unrestricted statement within the exactly-three-ones class: the source need not itself be a palindrome.

## Assumptions and scope

The source is a linear binary word with exactly three ones. A subsequence is obtained by deleting positions without reordering the rest. Distinct embeddings of the same string are counted once. The empty string is excluded. The bound holds also at \(z=0\), and the asymptotic constant in \(O(z)\) is absolute.

## Proof

### Counting input

The exact four-gap count appears in [1] (with the empty string included) and [2] (without it). We give the short derivation to specify the objective in the extremal problem. By reversal assume \(a\le d\), and write
\[
 h=d-a,\qquad p=b+c,\qquad m=\min(b,c),\qquad t=\min(b,h).
\]
There are \(z\) palindromes using no one. A palindrome using one one has the form \(0^i1 0^i\); its feasible \(i\)'s are the union of three initial intervals from the three source ones. This contributes \(H+1\), where
\[
 H=\max\{\min(a,b+c+d),\min(a+b,c+d),\min(a+b+c,d)\}.
\]
With two ones, the form is \(0^i1 0^j1 0^i\). The first/third pair realizes all \(0\le i\le a\) and \(0\le j\le p\), including every possibility from the first/second pair. The second/third pair adds precisely \(a<i\le \min(a+b,d)\), \(0\le j\le c\). Thus the two-one count is \((a+1)(p+1)+t(c+1)\). The three-one form \(0^i1 0^j1 0^j1 0^i\) has \(0\le i\le a,\ 0\le j\le m\), contributing \((a+1)(m+1)\). In particular,
\[
 P(w)=Q+z+H+2a+p+m+t+3,
 \qquad Q=a(p+m)+tc,
 \qquad z=2a+p+h.
\]
Since \(H,m\le z/2\) and \(2a+p+t\le z\), the nonquadratic part is between zero and \(3z+3\).

### Unrestricted extremal inequality

Optimize \(Q\) over nonnegative real gaps. If \(h\ge b\), then \(t=b\). At fixed \(z,b,c\), decreasing \(h\) to \(b\) increases \(a\) and cannot decrease \(Q\), so it suffices in this case to bound \(Q\) at \(h=b\). If \(b\le c\), put \(u=a+b\); then \(z=2u+c\) and
\[
 Q=2ab+uc\le \tfrac12u^2+uc=zu-\tfrac32u^2\le z^2/6.
\]
If \(b\ge c\), put \(e=b-c\). Using \(h=b\) and expanding gives
\[
 3z^2-16Q=12(a-c/2)^2+8c^2+8ae+20ce+12e^2>0\quad(z>0).
\]

If \(0\le h\le b\), put \(a=(z-b-c-h)/2\) and hold \(z,b,c\) fixed. When \(b\ge c\), \(Q=a(b+2c)+hc\) has slope \(-b/2\) as a function of \(h\); hence its maximum occurs at \(h=0\). When \(b\le c\), \(Q=a(2b+c)+hc\) has slope \(c/2-b\). A nonpositive slope again makes \(h=0\) a maximum. For positive slope the maximum is at \(h=\min(b,z-b-c)\). If \(h=b\) the preceding estimates apply, and otherwise \(a=0\), so \(Q=hc\le h(z-2h)\le z^2/8\), using \(h\le b\).

At \(h=0\) one has \(Q=a(p+m)\le(3/2)ap\le 3z^2/16\), since \(m\le p/2\) and \(2a+p=z\). Equality for \(z>0\) in this last bound requires \(b=c>0\) and \(2a=p=z/2\). When \(b=c>0\) the slope in the preceding reduction is strictly negative, so equality indeed requires \(h=0\). Together with the strict bounds in the other cases this proves
\[
 Q\le 3z^2/16,
 \qquad\text{with equality for }z>0\text{ exactly at }a=b=c=d=z/4.
\]

The counting input now gives the claimed upper bound on \(P\). In the exactly balanced word with gaps \(k,k,k,k\), it gives \(P=3k^2+11k+3\). Taking \(k=\lfloor z/4\rfloor\) and appending the leftover zeros cannot destroy a subsequence, giving \(M(z)\ge3z^2/16-O(z)\). For any maximizing sequence the uniform bound on \(P-Q\) thus gives \(Q/z^2\to3/16\). The normalized gaps lie in a compact simplex, and \(Q/z^2\) is a continuous function of them (write the reversed formula when \(a>d\); the expressions coincide on \(a=d\)). Every subsequential limit must therefore attain equality in the homogeneous inequality. Its sole equality point is the claimed limit.

## Reproducibility and relation to other results

The companion `verify.py` contains finite comparisons of the counting input with interval dynamic programming and literal subsequence sets, and finite scans for extremal counts. The proof above establishes the all-size bound and rigidity without extrapolation from those checks.

The counting identity is used here as an input, not claimed as a distinct enumeration result from [1] or [2]. The exact optimum among palindromic source words in [1] does not bound nonpalindromic sources; the uniform random-word limit of [2] does not locate the global maximizing gaps. The run-bounded theorem in [3] optimizes over all words with a fixed bound on runs. At seven runs its leading term is quartic. Its lower-run remainder bound does not determine the quadratic leading term when three of the run lengths are constrained to singleton ones. Counting the contributions from both two-one and three-one palindromes and controlling asymmetric gaps are essential to the extremal result here. General scattered-palindrome bounds in [4] do not use the fixed count of ones. These comparisons concern theorem coverage, not the chronology of discovery.

No exact finite formula for \(M(z)\) or complete list of finite-size maximizers is asserted. The theorem does not concern contiguous palindromic factors or alphabets with additional symbols.

## References

1. [A closed palindromic-subsequence count for three-one binary words](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-a-closed-palindromic-subsequence-count-for-three-one-binary-word--3fb9dc585778/RESULT.md), Finding and Proof.
2. [Exact scattered-palindrome complexity and limit law for binary words with three ones](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-exact-scattered-palindrome-complexity-and-limit-law-for-binary-w--bc05508b94e7/RESULT.md), Finding and Proof.
3. [Universal run-bounded asymptotics and rigidity for scattered palindromes](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-universal-run-bounded-asymptotics-and-rigidity-for-scattered-pal--24ceac73bbf9/RESULT.md), Finding and Proof.
4. K. Mahalingam and P. Pandoh, [Counting scattered palindromes in a finite word](https://arxiv.org/abs/2108.02729), Theorem 4.2 and Section 5.
