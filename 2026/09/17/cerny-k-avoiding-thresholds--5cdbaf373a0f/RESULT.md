# Exact k-avoiding thresholds of the Černý automata

## Statement

Let \(C_n\) be the standard \(n\)-state Černý automaton on
\(Q=\mathbb Z/n\mathbb Z\) with letters
\[
a:i\mapsto i+1\pmod n,
\qquad
b:i\mapsto\begin{cases}0,&i=n-1,\\ i,&0\le i\le n-2.\end{cases}
\]
For a subset \(S\subsetneq Q\), a word \(w\) *avoids* \(S\) when
\(\delta(Q,w)\cap S=\varnothing\).  Write \(\operatorname{at}_k(C_n)\) for the
maximum, over all \(k\)-subsets \(S\), of the length of a shortest word
avoiding \(S\).

**Theorem.** For every \(n\ge2\) and \(1\le k\le n-1\),
\[
\boxed{\operatorname{at}_k(C_n)=kn.}
\]
Moreover, with the above labeling the unique \(k\)-subset attaining this
maximum is
\[
B_k=\{n-k-1,n-k,\ldots,n-2\},
\]
and \((ba^{n-1})^k\) is a shortest word avoiding \(B_k\).

Thus the classical Černý series realizes an exact linear-in-\(k\) avoiding
threshold with coefficient \(n\), simultaneously for every admissible \(k\).

## Proof

For a set \(P\subseteq Q\), use inverse action notation
\(P\ell^{-1}=\delta^{-1}(P,\ell)\).  A word \(w\) avoids \(P\) exactly when
\(Pw^{-1}=\varnothing\).  The two inverse letter actions are
\[
Pa^{-1}=P-1
\]
and
\[
Pb^{-1}=\begin{cases}
P\setminus\{n-1\},& n-1\in P,\ 0\notin P,\\
P\cup\{n-1\},& 0\in P,\ n-1\notin P,\\
P,&\text{otherwise.}
\end{cases}
\tag{1}
\]

### Normal form for a shortest avoiding word

Consider a shortest inverse-action path from a nonempty target \(P\) to the
empty set.  It cannot use \(b^{-1}\) in either of the last two cases of (1).
If \(Pb^{-1}=P\), that step can simply be deleted.  If
\(Pb^{-1}=P\cup\{n-1\}\supset P\), and a subsequent inverse word \(u^{-1}\)
sends the larger set to the empty set, then the same subsequent inverse word
also sends \(P\) to the empty set because preimages preserve inclusion.
Deleting the enlarging \(b^{-1}\) again shortens the path.

Hence every occurrence of \(b^{-1}\) in a shortest inverse path deletes
exactly one state, namely \(n-1\).  Starting from a \(k\)-set, exactly \(k\)
such deletions are therefore required; all other steps are rotations by
\(a^{-1}\).

### Universal upper bound \(kn\)

Let \(P\) be any nonempty proper subset of the cycle.  There is a state
\(p\in P\) whose successor \(p+1\) is outside \(P\).  Choose
\(r\in\{0,1,\ldots,n-1\}\) with \(r\equiv p+1\pmod n\).  After \(r\) inverse
\(a\)-steps, the state \(p\) is at \(n-1\), while the absent state \(p+1\)
is at \(0\).  Therefore the next \(b^{-1}\) deletes \(n-1\).  This removes
one state using at most \((n-1)+1=n\) letters.

Repeating the argument until the target set is empty gives an avoiding word
of length at most \(kn\) for every \(k\)-set.  Thus
\(\operatorname{at}_k(C_n)\le kn\).

### A target that requires \(kn\)

Take
\[
B_k=\{n-k-1,\ldots,n-2\}.
\]
It is one consecutive occupied block, and its only state whose successor is
outside the block is \(n-2\).  In a shortest inverse path, the first
\(b^{-1}\) must be a deleting step by the normal-form argument.  Before that
first deletion there can therefore only be rotations.  A deleting
\(b^{-1}\) is possible precisely when an occupied-to-empty boundary has been
rotated to the edge \(n-1\to0\).  For \(B_k\), its unique such boundary is
\(n-2\to n-1\), which first reaches \(n-1\to0\) after exactly \(n-1\)
applications of \(a^{-1}\).

After those \(n-1\) rotations,
\[
B_k(a^{-1})^{n-1}=\{n-k,\ldots,n-1\},
\]
and one deleting \(b^{-1}\) leaves
\[
\{n-k,\ldots,n-2\}=B_{k-1}.
\]
Consequently, if \(d(P)\) denotes the shortest avoidance length for \(P\),
then
\[
d(B_k)\ge n+d(B_{k-1}),\qquad d(B_0)=0.
\]
Thus \(d(B_k)\ge kn\).  The inverse action of
\((ba^{n-1})^k\) performs exactly the deletion sequence above, so equality
holds.

### Uniqueness of the worst target

If a \(k\)-set \(P\ne B_k\), then it has an occupied-to-empty boundary
\(p\to p+1\) with \(p\ne n-2\).  (A nonempty proper cyclic subset with only
one occupied-to-empty boundary is one cyclic block; if that sole boundary is
\(n-2\to n-1\), its cardinality forces the block to be exactly \(B_k\).)
For such a boundary, \(r\equiv p+1\pmod n\) can be chosen with
\(0\le r\le n-2\).  Hence one state can be deleted using at most \(n-1\)
letters.  The remaining \(k-1\) states can be deleted using at most
\((k-1)n\) more letters by the universal construction.  Therefore
\[
d(P)\le kn-1.
\]
So \(B_k\) is the unique maximizer.

## Relation to prior work

Ferens, Szykuła and Vorel introduced and studied \(k\)-avoiding thresholds in
this form.  Their 2021 paper explicitly gives the four-state Černý example,
whose \(k=1,2,3\) thresholds are \(4,8,12\), and uses it to illustrate the
definition.  Their main results concern extremal avoiding thresholds over
broader automaton classes and leave the synchronizing case open for general
\(k\).  The theorem above extends that displayed Černý example to every
\(n\) and every \(k\), and identifies the unique worst target.

Szykuła's 2026 open-problems survey records the one-state fact for the Černý
automaton: the individual state-avoiding thresholds range up to \(n\).  The
formula above gives the full higher-\(k\) analogue.

Ferens and Szykuła's 2026 work on completely reachable automata notes that the
Černý automata meet Don's reaching bound \(n(n-|T|)\) by subset cardinality.
That statement is related but does not itself give the result here: avoiding a
set \(S\) only requires the final image to be *contained* in \(Q\setminus S\),
so a shorter word could in principle reach a proper subset of the complement.
The inverse-action argument rules out that shortcut for \(B_k\).

The preimage formulation used in the proof is standard: total extension of a
subset is equivalent to avoidance of its complement.

## Verification

`artifacts/verify_cerny_avoiding.py` performs exhaustive breadth-first search
in the image-subset automaton.  It was executed for every \(2\le n\le11\)
and every \(1\le k<n\).  In all 55 parameter pairs it confirms both
\(\operatorname{at}_k(C_n)=kn\) and the claimed unique maximizer \(B_k\).
The deterministic output is included in `artifacts/verification.txt`.
These computations are checks of finite cases; the theorem itself is proved
for all \(n,k\) above.

## Limitations and originality boundary

Originality is asserted only to the best of our knowledge.  The notions of
avoiding words, \(k\)-avoiding threshold, total extension, the Černý automata,
and Don-type reaching bounds are prior work.  The claimed contribution is the
all-\(n\), all-\(k\) exact formula for the Černý series together with the
unique extremal target and the inverse-boundary proof.  The 2021 source already
contains the complete \(n=4\) instance \(4,8,12\), so that special case is not
new.  The 2026 survey already states the \(k=1\) threshold \(n\), so that case
is also not new in isolation.

Searches were performed under `k-avoiding threshold`, `avoiding subset`,
`totally extending`, `included reachability`, `Černý automaton`, and equivalent
preimage terminology.  No prior general formula \(kn\) for all \(k\) was
located.  Older literature on circular/1-contracting automata and subset
reachability remains the most plausible residual coverage risk, because an
equivalent total-extension statement could have been recorded without the
later `k-avoiding` terminology.

Same-model review: passed. Cross-model review: not yet performed.

## References

1. R. Ferens, M. Szykuła, V. Vorel, *Lower Bounds on Avoiding Thresholds*, MFCS 2021. https://doi.org/10.4230/LIPIcs.MFCS.2021.46
2. M. Szykuła, *Synchronizing Automata: Open Problems*, 2026. https://arxiv.org/abs/2608.24245
3. R. Ferens, M. Szykuła, *Recognizing Completely Reachable Automata in Quadratic Time*, ACM Transactions on Algorithms 22(2), 2026. https://doi.org/10.1145/3798283
4. M. V. Berlinkov, R. Ferens, M. Szykuła, *Complexity of Preimage Problems for Deterministic Finite Automata*, MFCS 2018. https://doi.org/10.4230/LIPIcs.MFCS.2018.32
5. H. Don, *The Černý Conjecture and 1-Contracting Automata*, Electronic Journal of Combinatorics 23(3), 2016. https://doi.org/10.37236/5616
