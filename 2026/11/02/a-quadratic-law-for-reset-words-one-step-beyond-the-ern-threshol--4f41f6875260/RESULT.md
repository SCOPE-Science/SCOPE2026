# A quadratic law for reset words one step beyond the Černý threshold

## Finding

For every integer \(n\geq2\), let \(\mathcal C_n\) be the deterministic automaton with states \(Q=\{0,1,\ldots,n-1\}\), alphabet \(\{a,b\}\), and transitions
\[
\delta(x,a)=x+1\pmod n,\qquad
\delta(x,b)=\begin{cases}0,&x=n-1,\\x,&x\ne n-1.\end{cases}
\]
A word is a *reset word* if it sends all states to one state. Write
\[
U_n=b(a^{n-1}b)^{n-2},\qquad L_n=(n-1)^2.
\]
Then \(U_n\) is the **unique** reset word of length \(L_n\); there is no shorter reset word; and **exactly**
\[
\boxed{(n-2)^2+3}
\]
distinct reset words have length \(L_n+1\).

There is a complete structural classification of the latter words:

1. The two boundary extensions \(aU_n\) and \(U_na\).
2. The \(n-1\) words obtained by doubling exactly one occurrence of \(b\) in \(U_n\).
3. For every \(1\le j\le n-2\), replace the \(j\)-th displayed block \(a^{n-1}\) of \(U_n\) by \(a^i b a^{n-1-i}\), where \(1\le i\le n-2\) and \(i\ne j\).

These families are disjoint and exhaustive. Precisely one length-\(L_n+1\) reset word ends in state \(1\), namely \(U_na\); all others reset to state \(0\). When \(n=2\), the last family is empty, as intended.

## Assumptions and scope

States and letters are **labeled**, and different letter strings are counted separately. A word acts from left to right. There are no changes of alphabet, quotienting by automorphisms, multiplicity weights, or asymptotic approximations. The theorem concerns only lengths \(L_n\) and \(L_n+1\), for every \(n\ge2\); it does not claim an enumerator at larger lengths or for arbitrary synchronizing automata.

## Proof

**1. A rotating-frame description of inverse images.** Fix a terminal reset state \(t\in Q\). Read a proposed reset word *backwards*, starting from the inverse-image set \(S=\{t\}\). An inverse \(a\) rotates every member of \(S\) one step backwards modulo \(n\). Let \(r\) be the number of inverse \(a\)'s processed, reduced modulo \(n\), and use the rotating-frame set
\[
X=\{s+r\pmod n:s\in S\}.
\]
Reading an inverse \(a\) increments \(r\) and leaves \(X\) unchanged. Reading inverse \(b\) performs precisely this update:
\[
X\longleftarrow
\begin{cases}
X\cup\{r-1\pmod n\},& r\in X,\\
X\setminus\{r-1\pmod n\},& r\notin X.
\end{cases}
\tag{1}
\]
Indeed \(b\) fixes every state except \(n-1\), whose image is \(0\). Thus its inverse either adds, retains, or removes that predecessor, according to membership of \(0\) and \(n-1\) in \(S\).

**2. A sharp lower bound from first appearances.** Initially \(X=\{t\}\). A vertex can first enter \(X\) only when its clockwise successor is already in \(X\), because every addition in (1) goes from \(r\) to \(r-1\). Therefore the \(n-1\) vertices not initially in \(X\) have their *first appearances* in the forced order
\[
t-1,\ t-2,\ldots,\ t-(n-1)\pmod n.
\]
The corresponding productive inverse-\(b\) actions require the phases
\[
r=t,\ t-1,\ldots,\t-(n-2)\pmod n.
\]
Phase \(r\) starts at zero and can increase only through inverse \(a\)'s. Before the first productive inverse \(b\), at least \(t\) copies of \(a\) are required, since \(0\le t<n\). Between consecutive first appearances, advancing to the preceding residue requires at least \(n-1\) further copies of \(a\). At least \(n-1\) inverse-\(b\) actions are also necessary. Hence every reset word ending at \(t\) satisfies
\[
\#a\ \ge\ t+(n-2)(n-1),\qquad \#b\ \ge\ n-1,
\]
and so
\[
|w|\ge L_n+t.\tag{2}
\]
This argument remains valid even if some inverse-\(b\) actions remove vertices: first appearances still must follow the directed predecessor chain.

The palindrome \(U_n=b(a^{n-1}b)^{n-2}\) realizes the lower bound at \(t=0\). In reverse, its first \(b\) adds \(n-1\), each succeeding block of \(n-1\) copies of \(a\) advances phase to the next required residue, and the next \(b\) adds one more vertex. After its last \(b\), \(X=Q\). Equality in (2) for \(t=0\) forces every \(b\) to be a first appearance and every phase advance to be minimal; thus \(U_n\) is the unique shortest reset word.

**3. Classifying one letter of slack.** Suppose \(|w|=L_n+1\). By (2) its terminal state must be \(t=0\) or \(t=1\). There are only three count possibilities:

- At \(t=1\), equality in (2) forces a single inverse \(a\) before the first productive inverse \(b\), followed by the rigid minimal phase advances. This yields \(U_na\) in forward reading.
- At \(t=0\), with \(n-1\) inverse \(b\)'s, exactly one inverse \(a\) exceeds the sharp lower bound. An extra \(a\) cannot occur before a first appearance or between consecutive first appearances, since the intervening counts must be congruent respectively to \(0\) and \(n-1\) modulo \(n\), whereas a single added \(a\) changes the residue. It must follow the final productive inverse \(b\). This gives \(aU_n\) in forward reading.
- At \(t=0\), with \(n\) inverse \(b\)'s, the inverse \(a\) count is minimal. There are exactly \(n-1\) first-appearance actions and one other inverse \(b\). The extra action cannot remove a vertex: removal would require an additional inverse \(b\) to re-add that vertex before obtaining \(X=Q\). Thus it must be **neutral**, leaving \(X\) unchanged. The productive actions and phase advances form the unique skeleton \(U_n\), with one extra neutral \(b\) inserted.

**4. Locating neutral insertions.** Number the productive inverse \(b\)'s from \(1\) to \(n-1\). Just after the \(j\)-th one, for \(1\le j\le n-2\), the rotating-frame state and phase are
\[
X_j=\{0,n-1,n-2,\ldots,n-j\},\qquad r_j=1-j\pmod n.
\]
Let \(h\in\{1,\ldots,n-2\}\) be the number of inverse \(a\)'s read after this action, before the next productive \(b\). Formula (1) shows that another \(b\) is neutral except when \(h=j\): in that case \(r=1\), so \(r\notin X_j\) but \(r-1=0\in X_j\), and the action removes \(0\). At the endpoints of the inter-\(b\) block, inserting \(b\) creates a doubled \(b\), which is valid because the first of the two can be productive and the second neutral. Doubling either initial or final \(b\) is likewise valid. Reversing the word preserves \(U_n\) as a palindrome; the forbidden split of its \(j\)-th \(a\)-block in forward reading has index \(i=j\).

Thus there are \(n-1\) distinct doubled-\(b\) words, and \((n-2)(n-3)\) distinct interior split words. The two boundary extensions are distinct from these and from each other. Their sum is
\[
2+(n-1)+(n-2)(n-3)=(n-2)^2+3.
\]
Distinctness is immediate from the run positions of \(b\), with boundary \(a\) extensions distinguished by their first or last letter. The classification and terminal-state assertion follow. \(\square\)

## Verification

The standalone `verify.py` independently implements the forward subset automaton using exact integer word counts at every length. It compares the complete distribution of reset targets at the shortest and next-shortest lengths for every \(2\le n\le13\), then checks that all explicitly described words reset and that the asserted families contain no duplicates. For \(2\le n\le8\), it additionally uses reverse-distance-pruned exhaustive enumeration of **every** reset word at length \(L_n+1\) and compares the literal word set to the structural classification. Successful output ends with `VERIFY_OK`. These are finite checks only; the infinite-parameter theorem follows from the proof, not the experiments.

Reproduce using a Python 3 interpreter, with no packages beyond the standard library:

```sh
python3 verify.py
```

## Relationship to prior work

The classical Černý family and its extremal reset threshold are standard; neither that threshold nor the shortest example word is claimed as new. Szykuła's 2017 preprint (arXiv:1702.05455, Sections 1–3) studies general upper bounds and avoiding words, presenting the four-state Černý example, not the second-shortest reset-word enumerator. Szykuła and Zyzik (arXiv:2207.05495, Sections 1–3) develop efficient exact algorithms for **finding a shortest reset length**, without stating the family-wide number or classification of words one step above it. Rodaro (arXiv:1708.04864, Sections 3–5) studies the language of factor-minimal reset words and general regular ideals, but does not derive this labeled, length-specific enumeration.

The result is a precise first-order stability statement for an extremal synchronizing automaton: a unique shortest reset word gives way to exactly quadratic—not exponential—many words at one extra letter. General automaton algorithms can compute each fixed instance, but their existence does not directly supply this closed all-parameter law.

## Limitations

The theorem uses a specific labeled presentation of the classical Černý family; isomorphic relabelings preserve the count, but changing transitions need not. The theorem says nothing about the number of reset words at \(L_n+2\) or greater lengths. A previously unlocated specialized language-enumeration identity might imply the formula; independent literature validation has not been performed.

## References

- Marek Szykuła, *Improving the upper bound on the length of the shortest reset words*, arXiv:1702.05455, first public version 2017-02-17; published in STACS 2018, DOI 10.4230/LIPIcs.STACS.2018.56.
- Emanuele Rodaro, *Synchronizing automata and the language of minimal reset words*, arXiv:1708.04864, first public version 2017-08-16.
- Marek Szykuła and Adam Zyzik, *An Improved Algorithm for Finding the Shortest Synchronizing Words*, arXiv:2207.05495, first public version 2022-07-03.
