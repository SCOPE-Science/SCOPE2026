# A single exceptional semicircle in a family of Bernoulli generating partitions

## Finding

Let \(T(x)=2x\pmod1\) on \([0,1)\) with Lebesgue probability, and for \(0\le a<1/2\) put \(I_a=[a,a+1/2)\). Record \(Z_n(x)={\bf1}_{I_a}(T^n x)\) at times \(n\ge0\). For **every real** \(a\) in this range, \((Z_n)_{n\ge0}\) is a sequence of independent fair Bernoulli variables.

Now restrict to dyadic \(a=k/2^r\), integers \(r\ge2\) and \(0\le k<2^{r-1}\). Then the observation map \(\Pi_a:x\mapsto (Z_0,Z_1,\ldots)\) is an almost-everywhere invertible measure-theoretic conjugacy from the Lebesgue doubling system to the one-sided fair Bernoulli shift **if and only if** \(a\ne1/4\). For each \(a\ne1/4\) there is a deterministic future-reading inverse with an exponentially decaying coding delay. Explicitly, set \(m=r-1\), \(L=2m+1\). An occurrence of the output word \(w=0^m10^m\) fixes the source state at the beginning of that word regardless of its subsequent binary digits. If \(D\) denotes the number of future observations needed to recover the initial \(m\)-bit source state using the first aligned occurrence of this word, then for every integer \(j\ge1\),

\[
\Pr(D>Lj)\le(1-2^{-L})^j.
\]

At the unique exceptional parameter \(a=1/4\), the output is still exactly independent and fair, but \(\Pi_{1/4}\) is **exactly two-to-one** on a set of full Lebesgue measure: its two preimages are \(x\) and \(1-x\pmod1\). Thus all placements yield the same complete output distribution while their ability to reconstruct the generating state differs sharply.

## Assumptions and scope

The circle coordinate uses representatives in \([0,1)\) and half-open intervals to fix endpoint conventions. The statements about binary expansions and multiplicity are made off the countable set of dyadic expansions and the corresponding negligible forward/preimage boundary sets. The source measure is Lebesgue, and the output probability is its pushforward. Only the generating-versus-two-to-one classification is restricted to dyadic \(a\); the independent-and-fair assertion holds for arbitrary real \(a\in[0,1/2)\). Finite parameters \(r\) and \(k\) are fixed, with no uniform claim as \(r\to\infty\).

## Proof

**1. Exactly independent output for any semicircle.** Conditional on \(T(x)=u\), a uniform starting point \(x\) takes its two inverse-branch values \(u/2\) and \((u+1)/2\) with equal conditional probabilities. Exactly one belongs to \(I_a\), except at measure-zero boundaries, because \(I_a\) and \(I_a+1/2\) partition the circle. Consequently \(\Pr(Z_0=1\mid T(x))=1/2\) almost surely. Every \(Z_j\) for \(j\ge1\) is measurable with respect to \(T(x)\), so \(Z_0\) is independent of the entire future output. Since doubling preserves Lebesgue measure, stationarity and iteration imply that each finite output word has probability \(2^{-\ell}\), where \(\ell\) is the word length.

**2. Exact threshold transducer.** Write \(x=0.b_0b_1b_2\ldots\) in binary. Put \(M=2^m\), \(m=r-1\), and \(k=2^r a\). Let \(s_n\in\{0,\ldots,M-1\}\) be the integer with \(m\)-bit binary expansion \(b_n\ldots b_{n+m-1}\). A comparison of the \(r\)-bit dyadic cells with the translated half interval gives

\[
Z_n=b_n\mathbin{\oplus}{\bf1}_{\{s_{n+1}\ge k\}},\qquad
s_n=F_{Z_n}(s_{n+1}),
\]

with the **backward-state maps**

\[
F_z(s)=\left\lfloor\frac{s}{2}\right\rfloor
+\frac M2\bigl(z\mathbin{\oplus}{\bf1}_{\{s\ge k\}}\bigr),
\quad s\in\{0,\ldots,M-1\},\ z\in\{0,1\}.
\]

All formulas use ordinary integers and Boolean exclusive-or. In particular, for a known future output segment \(z_n\ldots z_{n+t-1}\), the present state is \(F_{z_n}\circ\cdots\circ F_{z_{n+t-1}}(s_{n+t})\).

**3. A universal reset word outside one cutoff.** For \(0<k<M\), \(F_0(s)=\lfloor s/2\rfloor\) when \(s<k\), and \(F_0(s)=M/2+\lfloor s/2\rfloor\) when \(s\ge k\). Each of these two regions is invariant. The former approaches \(0\), the latter approaches \(M-1\), and exactly \(m\) iterations suffice, since the distance to the applicable endpoint is halved with integer rounding at every step. Thus

\[
F_0^m(s)=\begin{cases}0,&s<k,\\M-1,&s\ge k.\end{cases}
\]

When \(k=0\), instead \(F_0^m\) is constantly \(M-1\). For \(0<k<M\), the middle letter acts on the two possible endpoint states by

\[
F_1(0)=M/2,\qquad F_1(M-1)=M/2-1.
\]

If \(k<M/2\), these lie in the upper region \(s\ge k\); if \(k>M/2\), both lie in the lower region \(s<k\). It follows that \(F_0^m\circ F_1\circ F_0^m\) is the constant map to \(M-1\) for \(0\le k<M/2\), and to \(0\) for \(M/2<k<M\). This is precisely the map associated with the palindromic word \(w=0^m10^m\), because the order in which an output word is read matches function composition from right to left.

In particular any occurrence of \(w\) at time \(t\) specifies \(s_t\) without knowing \(s_{t+L}\). Applying the known maps \(F_{Z_0},\ldots,F_{Z_{t-1}}\) backwards recovers \(s_0\). Likewise, looking from any fixed time \(n\), a later occurrence of \(w\) recovers \(s_n\), hence \(b_n\), the leading bit of this state. Since the outputs are independent fair bits, the word appears infinitely often almost surely. Thus every binary input digit can be recovered measurably from the output, and the map is invertible modulo null sets; shift commutation makes it a measure-theoretic conjugacy.

Divide the output into aligned disjoint blocks of length \(L\). They equal \(w\) independently with probability \(2^{-L}\). If the first successful block is one of the first \(j\) blocks, the state \(s_0\) is determined from the first \(Lj\) outputs. This proves the displayed exponential tail. The same bound applies after every fixed time \(n\) by stationarity.

**4. The exceptional cutoff.** If \(k=M/2\), then \({\bf1}_{\{s_{n+1}\ge k\}}=b_{n+1}\), because the first bit of \(s_{n+1}\) is \(b_{n+1}\). Thus

\[
Z_n=b_n\mathbin{\oplus} b_{n+1}.
\]

For a specified output sequence, choosing \(b_0\in\{0,1\}\) determines all subsequent bits recursively via \(b_{n+1}=b_n\oplus Z_n\). The two choices produce complementary binary expansions, corresponding to points \(x\) and \(1-x\pmod1\) for non-eventually-constant expansions. Every typical output therefore has exactly two input preimages. This rules out a one-sided generating partition precisely at \(a=1/4\).

## Verification

Run the standalone `verify.py` with Python 3; no nonstandard dependencies are required. The checker exhaustively compares the analytic backward-state formula with forward binary-word coding for small finite parameters; evaluates the reset map on every state through modulus \(M=512\); proves its counted images are singleton except at the quarter cut; and enumerates short independent-output word probabilities for finite binary sources. The mathematical statements for arbitrary parameters and infinite time follow from the preceding proof, not from a bounded computation. The geometric-tail bound uses disjoint Bernoulli blocks and is exact for the tested block events.

## Relationship to prior work

Sliding-block representations of shift-commuting maps and the classical Curtis–Hedlund–Lyndon framework precede this result. Gonçalves, Sobottka and Starling's treatment of sliding-block codes over infinite alphabets gives a more general coding framework, not an explicit invertibility classification of translated dyadic semicircle sensors for doubling. The general notion of a synchronizing deterministic automaton and a reset word is well established; Araújo, Cameron and Steinberg survey it, but do not give the comparator-state reset or exceptional parameter in this family. General Bernoulli-isomorphism results do not decide whether **this prescribed binary partition** itself generates or give its finite-delay decoder. The contribution here is the complete unbounded dyadic parameter classification, the explicit reset word and tail bound, and the observation that all associated factor processes have indistinguishable joint distributions.

## Limitations

The multiplicity classification is proved for dyadic cuts only. The existence, size and regularity of a coding inverse for irrational or other nondyadic cuts is not classified. The inverse is almost-sure and finitary, not claimed to be a topological conjugacy on every binary string. Its geometric tail constant depends exponentially on the dyadic precision \(r\). Historical priority remains uncertain because general finite-state factor and synchronizing-code machinery may contain implicit specializations; no claim of independent novelty certification is made.

## References

1. D. Gonçalves, M. Sobottka and C. Starling, *Sliding block codes between shift spaces over infinite alphabets*, arXiv:1502.06262v1 (first posted 22 February 2015). https://arxiv.org/abs/1502.06262 . The primary MSC2020 assignment of the motivating symbolic-coding literature is 37B10.
2. J. Araújo, P. J. Cameron and B. Steinberg, *Between primitive and 2-transitive: Synchronization and its friends*, arXiv:1511.03184v1 (10 November 2015). https://arxiv.org/abs/1511.03184 .
3. Classical binary-expansion model of the doubling transformation and the fair Bernoulli shift; both foundational and used as established background.
