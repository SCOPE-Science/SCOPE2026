# Fixed hidden alphabets preserve almost all finite-language projection blow-up

## Result

Let \(k\ge 3\) be the size of the projected alphabet and let \(h\ge2\) be fixed. Put
\[
t=\lceil\log_2 k\rceil.
\]
For every sufficiently large integer \(N\), set
\[
m=\left\lfloor\frac{N}{t+1}\right\rfloor,\qquad
L=N-m-1,
\]
and
\[
J=\max\left\{0,\left\lceil\frac{L-h}{h-1}\right\rceil\right\},\qquad
n_N=N+J.
\]
Then there is a finite language \(K_{N,h}\) over an alphabet of size \(k+h\), recognized by a minimal incomplete DFA with exactly \(n_N\) states, and a projection \(P\) onto the \(k\) visible symbols such that
\[
\boxed{
\|P(K_{N,h})\|\ge
\frac{k^{m+1}-1}{k-1}-1.
}
\]
Here \(\|M\|\) denotes the number of states in a minimal incomplete DFA for a regular language \(M\).

Consequently, along this infinite family,
\[
\|P(K_{N,h})\|
=\Omega\!\left(k^{\alpha_{k,h}n_N}\right),
\qquad
\alpha_{k,h}=\frac{h-1}{(t+1)(h-1)+t}.
\]
Relative to the exponent \(1/(t+1)\) in the Jirásková--Masopust growing-domain witness, the retained fraction is
\[
\rho_{t,h}
=\frac{(t+1)(h-1)}{(t+1)(h-1)+t}.
\]
Thus, for every \(0<\varepsilon<1\), choosing the fixed value
\[
h=1+\lceil1/\varepsilon\rceil
\]
gives \(\rho_{t,h}>1-\varepsilon\). In particular, the domain alphabet can be bounded independently of the state count while retaining an arbitrarily large fraction of the known exponential lower-bound rate.

When \(k\) is a power of two, \(t=\log_2 k\), so these fixed-domain families approach arbitrarily closely the exponent \(1/(1+\log_2 k)\) appearing in the optimal worst-case determinization bound for finite \(k\)-letter NFAs.

This is a quantitative partial answer to the constant-domain-alphabet question stated by Jirásková and Masopust. It does not prove that their exact exponent can be attained with one fixed domain alphabet.

## Construction

Jirásková and Masopust use a visible \(N\)-state chain over
\[
\Sigma_o=\{0,1,\ldots,k-1\}
\]
and add \(L=N-m-1\) distinct erased symbols, each giving a direct transition from the initial state \(q_0\) to one of
\[
q_1,q_2,\ldots,q_L.
\]
After projection, this direct fan-out makes all those states simultaneously available by \(\varepsilon\)-reachability and yields their finite-language lower bound.

Replace those \(L\) distinct erased symbols by a fixed erased alphabet
\[
\Gamma=\{\gamma_1,\ldots,\gamma_h\}.
\]
From \(q_0\), build a rooted deterministic \(h\)-ary routing tree whose leaves are the existing states \(q_1,\ldots,q_L\). The tree uses exactly \(J\) fresh internal states. Its edges are labeled by symbols of \(\Gamma\), reusing the same \(h\) labels at different internal states. Fresh internal states have no visible transitions, and the original chain states receive no new erased outgoing transitions.

Because every routing edge is erased, the \(\varepsilon\)-closure of \(q_0\) contains exactly the same original chain states \(q_0,q_1,\ldots,q_L\) as in the direct-fan-out construction, together with routing states that have no visible behavior. After the first visible symbol, no new erased transition is available. Therefore the projected language is exactly the projected language of the original direct-fan-out witness.

The resulting automaton is acyclic: routing edges move outward in the tree, while visible transitions move strictly forward along the chain. Hence its language is finite.

## Exact routing overhead

The value
\[
J=\max\left\{0,\left\lceil\frac{L-h}{h-1}\right\rceil\right\}
\]
is not merely sufficient; it is optimal for deterministic routing-only replacement of a one-source silent fan-out.

Indeed, suppose \(J'\) fresh routing states and the root are the only states allowed to emit the \(h\) erased symbols, and all \(L\) target states must be reachable by erased-only paths. Every fresh routing state needs an incoming erased edge, and every target needs an incoming erased edge, so there are at least \(J'+L\) such edges. Determinism permits at most \(h(J'+1)\) erased outgoing edges from the root and routing states. Hence
\[
J'+L\le h(J'+1),
\]
which gives
\[
J'\ge\left\lceil\frac{L-h}{h-1}\right\rceil
\]
when \(L>h\). A partially filled \(h\)-ary tree attains equality.

## Minimality of the input DFA

The \(N\) original chain states remain pairwise distinguishable: from \(q_i\), every accepted visible continuation has the chain-determined length \(N-1-i\), and at least one such continuation exists.

A fresh routing state is distinguishable from every original chain state because any accepting computation from the routing state must begin with an erased routing symbol, whereas each chain state has a visible-only accepting continuation (with the final state accepting the empty word).

For two distinct routing states \(u\) and \(v\), choose an erased word \(x\) taking \(u\) to a descendant leaf \(q_i\). Reading the same \(x\) from \(v\) is either undefined, ends at a routing state, or reaches a different leaf \(q_j\). Appending a visible accepting continuation of \(q_i\), whose length is unique to \(q_i\), distinguishes the two states. Thus all \(N+J\) states are inequivalent.

## Asymptotic calculation

Since
\[
m=\frac{N}{t+1}+O(1)
\]
and
\[
J=\frac{N-m}{h-1}+O(1)
 =\frac{tN}{(t+1)(h-1)}+O(1),
\]
we have
\[
n_N=N\left(1+\frac{t}{(t+1)(h-1)}\right)+O(1).
\]
Inverting this relation gives
\[
m=\frac{h-1}{(t+1)(h-1)+t}\,n_N+O(1),
\]
and the displayed exponential lower bound follows.

Moreover,
\[
1-\rho_{t,h}
=\frac{t}{(t+1)(h-1)+t}.
\]
If \(h-1\ge1/\varepsilon\), then \(1-\rho_{t,h}<\varepsilon\).

## Verification

The accompanying finite verifier reconstructs the Jirásková--Masopust visible-chain witness, replaces the direct erased fan-out by the fixed-alphabet tree, determinizes the projection using erased-symbol closure, and minimizes the constructed input DFA. It checks 63 parameter triples with
\[
k\in\{3,4,5\},\quad h\in\{2,3,4\},\quad N\in\{6,\ldots,12\}.
\]
For every checked case, the input DFA has exactly the claimed number of minimal states. After deleting inert routing states from projected subset states, the compressed construction has exactly the same reachable visible-subset transition system and accepting status as the direct-fan-out construction; the projected state count also meets the geometric lower bound above.

## Significance

The 2012 projection paper explicitly notes that its finite-language witness uses a domain alphabet whose size grows linearly with the number of states and leaves open whether the domain alphabet can be bounded by a constant. The construction here shows that the growing family of erased symbols can be replaced by a fixed erased alphabet at linear state overhead, with an exact optimal overhead in the natural routing-only model. Increasing the fixed hidden alphabet makes that overhead arbitrarily small as a fraction of the witness size, so an arbitrarily large fraction of the known exponential blow-up rate survives under a state-independent domain alphabet bound.

## Limitations

- This does not settle whether the exact Jirásková--Masopust finite-language exponent is attainable with one fixed domain alphabet.
- The quantitative comparison uses their specific finite-language witness and its known lower bound; it is not a universal lower bound for every projected finite language.
- Originality is to the best of our knowledge. The checked later literature includes work on projection for permutation and commutative automata, binary coding of regular languages, and recent finite/block-language state complexity. None of the inspected sources states this fixed-hidden-alphabet routing construction or its near-preservation bound.
- Reference [31] of the 2012 paper is a 2011 personal communication by Kai Salomaa on finite-language NFA-to-DFA conversion and was not available as a public paper. It remains a residual originality risk for unpublished refinements of the finite-language determinization bound.

## References

1. G. Jirásková, T. Masopust, *State Complexity of Projected Languages*, DCFS 2011, LNCS 6808, 198--211. https://doi.org/10.1007/978-3-642-22600-7_16
2. G. Jirásková, T. Masopust, *On a structural property in the state complexity of projected regular languages*, Theoretical Computer Science 449 (2012), 93--105. https://doi.org/10.1016/j.tcs.2012.04.009
3. K. Salomaa, S. Yu, *NFA to DFA Transformation for Finite Languages over Arbitrary Alphabets*, Journal of Automata, Languages and Combinatorics 2(3) (1997), 177--186. https://dblp.org/rec/journals/jalc/SalomaaY97
4. S. Hoffmann, *State Complexity of Projection on Languages Recognized by Permutation Automata and Commuting Letters*, DLT 2021, LNCS 12811, 192--203. https://doi.org/10.1007/978-3-030-81508-0_16
5. S. Hoffmann, *State complexity bounds for projection, shuffle, up- and downward closure and interior on commutative regular languages*, Information and Computation 301 (2024), 105204. https://doi.org/10.1016/j.ic.2024.105204
6. V. Geffert, D. Pališínová, A. Szabari, *State complexity of binary coded regular languages*, Theoretical Computer Science 990 (2024), 114399. https://doi.org/10.1016/j.tcs.2024.114399
7. G. Duarte, N. Moreira, L. Prigioniero, R. Reis, *Operational State Complexity of Block Languages*, EPTCS 407 (2024), 59--76. https://doi.org/10.4204/EPTCS.407.5
