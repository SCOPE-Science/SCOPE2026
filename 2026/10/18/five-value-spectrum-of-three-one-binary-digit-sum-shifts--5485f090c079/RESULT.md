# Five-value spectrum of three-one binary digit-sum shifts

## Finding
Let \(s_2(n)\) denote the number of ones in the base-two expansion of a nonnegative integer, and let
\[
c_t=\lim_{N\to\infty}\frac{1}{N}\#\{0\le n<N:s_2(n+t)\ge s_2(n)\},\qquad t\ge1.
\]
For every \(t\) with exactly three nonzero binary digits, write uniquely
\[
t=2^e(1+2^b+2^a),\qquad e\ge0,\quad a>b\ge1.
\]
Put \(g=b-1\), \(h=a-b-1\), \(G=\min(g,3)\), and \(H=\min(h,3)\). Then \(c_t\) depends only on \((G,H)\), and its complete exact value table is

| \(G\) / \(H\) | \(0\) | \(1\) | \(2\) | \(3\) |
|:--|:--:|:--:|:--:|:--:|
| \(0\) | \(43/64\) | \(19/32\) | \(41/64\) | \(21/32\) |
| \(1\) | \(19/32\) | \(5/8\) | \(5/8\) | \(41/64\) |
| \(2\) | \(41/64\) | \(5/8\) | \(5/8\) | \(41/64\) |
| \(3\) | \(21/32\) | \(41/64\) | \(41/64\) | \(21/32\) |

Thus the value set is exactly
\[
\left\{\frac{19}{32},\frac58,\frac{41}{64},\frac{21}{32},\frac{43}{64}\right\}.
\]
In particular,
\[
\min_{s_2(t)=3}c_t=\frac{19}{32},\quad
c_t=\frac{19}{32}\ \Longleftrightarrow\ t\in\{11\cdot2^e,13\cdot2^e:e\ge0\},
\]
and \(c_t\) attains its maximum \(43/64\) exactly when \(t=7\cdot2^e\) for some \(e\ge0\).

## Assumptions and scope
All variables \(n,t,a,b,e,g,h,G,H\) are integers in the ranges above. The index \(G=3\) (respectively \(H=3\)) means the corresponding zero gap has **at least** three digits, not exactly three. The theorem is for all positive shifts with precisely three one-bits, with no bound on their positions. The density is natural density, not a finite-sample frequency; its existence follows from the proof.

## Proof
**Carry identity.** For binary digits \(x_i\in\{0,1\}\) of \(n\) and \(t_i\in\{0,1\}\) of \(t\), let the incoming carry be \(u_0=0\) and define
\[
u_{i+1}=\left\lfloor\frac{x_i+t_i+u_i}{2}\right\rfloor\in\{0,1\}.
\]
Adding the column equations \(x_i+t_i+u_i=y_i+2u_{i+1}\) over all columns, where \(y_i\) are the binary digits of \(n+t\), gives
\[
s_2(n+t)-s_2(n)=s_2(t)-\sum_{i\ge0}u_{i+1}.
\]
Only finitely many carries occur in an ordinary finite sum. When \(s_2(t)=3\), the desired event is therefore equivalent to at most three outgoing carries in total.

**Truncation of zero gaps.** A zero digit of \(t\) cannot create a carry when its incoming carry is zero, regardless of \(x_i\). At the start of a zero run, if the incoming carry is one, it was already counted at the preceding column. If it persists through three zero columns, at least four outgoing carries have occurred (the preceding one plus the three new ones), and that path is excluded. Consequently every path contributing to the event has zero outgoing carry after the first three zeros in any internal gap; all later zeros in that gap are inert. Thus a zero run of any length at least three may be replaced by exactly three zeros **without changing the density**. The identical argument shows that, after the highest one-bit of \(t\), three additional zero columns suffice: accepted paths have no outgoing carry beyond them, and rejected paths cannot subsequently become accepted.

Finally, \(c_{2t}=c_t\): write \(n=2q+r\), \(r\in\{0,1\}\). Then \(s_2(n+2t)-s_2(n)=s_2(q+t)-s_2(q)\), in both residue classes of \(n\). Iteration removes the factor \(2^e\). Therefore it suffices to analyze the finite low-to-high digit word consisting of one, \(G\) zeros, one, \(H\) zeros, one, and three trailing zeros, of length
\[
L=6+G+H.
\]
For this word, the acceptance event depends exactly on the first \(L\) bits of \(n\). Hence it is a union of residue classes modulo \(2^L\), establishing existence and rationality of its natural density.

**Exact finite transfer.** Let \(A_i(u,m)\) count prefixes of \(i\) choices of bits of \(n\) leaving carry \(u\in\{0,1\}\) and exactly \(m\) outgoing carries, discarding \(m>3\). Initially \(A_0(0,0)=1\) and all other entries vanish. For each of the \(L\) columns with prescribed shift bit \(t_i\), take both \(x=0\) and \(x=1\) and perform the integer update
\[
u'=\left\lfloor\frac{x+t_i+u}{2}\right\rfloor,\qquad
A_{i+1}(u',m+u')\mathrel{+}=A_i(u,m),\quad m+u'\le3.
\]
Here \(A_{i+1}\) is reset to zero before each column. The exact number of successful residues is \(N_{G,H}=\sum_{m=0}^3A_L(0,m)\), and \(c_t=N_{G,H}/2^L\). The complete integer table obtained by these six-or-more explicitly specified updates is

| \(G\) / \(H\) | \(0\) | \(1\) | \(2\) | \(3\) |
|:--|--:|--:|--:|--:|
| \(0\) | 43 | 76 | 164 | 336 |
| \(1\) | 76 | 160 | 320 | 656 |
| \(2\) | 164 | 320 | 640 | 1312 |
| \(3\) | 336 | 656 | 1312 | 2688 |

Dividing entry \((G,H)\) by \(2^{6+G+H}\) yields the displayed rational table. Comparing all sixteen exact entries shows the five-value spectrum and both sharp equality classifications. This proves the theorem. \(\square\)

## Verification
The supplied stand-alone `verify.py` uses only the Python standard library and can be run as `python3 verify.py`. It implements the integer transfer above, checks all sixteen prescribed counts and all five resulting rational values, and independently enumerates **every** residue modulo \(2^{6+G+H}\) for every one of the sixteen canonical cases, checking the original inequality with native exact integer binary weights. It additionally checks all 169 pairs \(0\le g,h\le12\) against the gap-truncation formula and confirms shift scaling. It reports `VERIFY_OK`. These finite calculations are certificates for the sixteen transfer entries; the zero-run argument, not the experiments, proves the reduction from arbitrarily large gaps to sixteen cases.

## Relationship to prior work
Drmota, Kauers and Spiegelhofer introduced this density framework, proved a distributional almost-all theorem, and gave a recurrence for the full shift-difference distribution and numerical values at specific small shifts [1]. Those methods compute individual shifts, but the inspected theorem statements and relevant recurrence/table do not state the uniform sixteen-case classification or its sharp equality set. Spiegelhofer and Wallner investigated shifts with many maximal blocks of ones [2], rather than this exact three-one case. Cheng subsequently established a universal positive bias bound \(c_t\ge1/2+2^{-2s_2(t)-1}\) [3], which implies positivity here but not the much stronger exact five-value spectrum or the minimizers. Cheng's later asymptotic fixed-Hamming-weight extremal theorem [4] concerns \(s_2(t)=k\) as \(k\to\infty\) and does not, in its accessible statements, determine the finite \(k=3\) spectrum. This theorem **does not claim** to prove Cusick's general conjecture, which has already been resolved in [3].

## Limitations
The theorem concerns shifts with exactly three nonzero binary digits. It neither classifies the complete distribution of digit-sum changes nor provides the spectrum for arbitrary fixed Hamming weight. The exact table was independently certified but not externally audited. The full text of the closely related 2026 fixed-weight paper [4] could not be obtained during the literature check; its accessible abstract and detailed secondary synopsis indicate a large-weight asymptotic result rather than this finite classification, but an unindexed stronger theorem or a finite appendix remains a residual originality risk.

## References
[1] M. Drmota, M. Kauers, L. Spiegelhofer, *On a Conjecture of Cusick Concerning the Sum of Digits of n and n+t*, arXiv:1509.08623, initial public version 2015-09-29. https://arxiv.org/abs/1509.08623

[2] L. Spiegelhofer, M. Wallner, *The binary digits of n+t*, arXiv:2005.07167, first posted 2020, revised 2022. https://arxiv.org/abs/2005.07167

[3] K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398 (2026). https://arxiv.org/abs/2606.23398

[4] K. Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899 (2026). https://arxiv.org/abs/2608.25899
