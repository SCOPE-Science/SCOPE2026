# Strict order-refinement monotonicity for canonical finite inquisitive algebras

## Finding
Let \(P=(W,\le_P)\) and \(Q=(W,\le_Q)\) be finite posets on the same \(n\)-element carrier, and write
\[
\mathcal I(P)=\operatorname{Dw}^{+}(\operatorname{Up}(P))
\]
for the canonical finite core-generated well-connected inquisitive algebra in Quadrellaro's representation. If \(\le_P\subsetneq\le_Q\), then
\[
\boxed{|\mathcal I(Q)|<|\mathcal I(P)|.}
\]
Thus **every genuine refinement of the Kripke order strictly shrinks the canonical algebra**.

The same carrier is used for the canonical dependence-algebra expansion, so the strict inequality holds there as well.

As a sharp consequence, for every finite \(n\)-point frame \(P\),
\[
\boxed{n+1\le |\mathcal I(P)|\le M_n-1,}
\]
where \(M_n\) is the \(n\)-th Dedekind number. The lower equality holds exactly for chains, and the upper equality exactly for antichains. Hence the two extremal carrier sizes begin
\[
\begin{array}{c|ccccc}
n&1&2&3&4&5\\\hline
\text{chain}&2&3&4&5&6\\
\text{antichain}&2&5&19&167&7580.
\end{array}
\]

## Assumptions and scope
The source associates to a finite poset \(P\) the lattice \(\operatorname{Up}(P)\) of upsets, ordered by inclusion, and then takes the nonempty downsets \(\operatorname{Dw}^{+}(\operatorname{Up}(P))\) as the carrier of the canonical inquisitive algebra. The core consists of the principal downsets. For dependence algebras the tensor operation is added to this same carrier.

Here an **order refinement** means adding comparabilities on a fixed carrier while retaining a partial order: \(\le_P\subsetneq\le_Q\). No claim is made that the comparison below is an inquisitive-algebra homomorphism, or that order refinement is a morphism in the source's dual category. The result is a cardinality theorem across canonical representations.

The Dedekind endpoint is classical: \(M_n\) counts all downsets of the Boolean lattice \(2^{[n]}\). Its use here is not claimed as new.

## Proof
Because \(Q\) has at least as many comparabilities as \(P\), every \(Q\)-upset is a \(P\)-upset. Therefore
\[
L_Q:=\operatorname{Up}(Q)\subseteq L_P:=\operatorname{Up}(P)
\]
as inclusion-ordered posets. The containment is strict. Indeed, choose \(a,b\in W\) with
\[
a\le_Q b\quad\text{but}\quad a\not\le_P b.
\]
Then the principal \(P\)-upset \(\uparrow_P a\) contains \(a\) but not \(b\), so it is not a \(Q\)-upset.

For every nonempty downset \(D\subseteq L_Q\), define
\[
\Phi(D)=\downarrow_{L_P}D
=\{A\in L_P:\text{ for some }B\in D,\ A\subseteq B\}.
\]
This is a nonempty downset of \(L_P\). Moreover,
\[
\Phi(D)\cap L_Q=D.
\]
The inclusion \(D\subseteq\Phi(D)\cap L_Q\) is immediate. Conversely, if \(A\in L_Q\cap\Phi(D)\), then \(A\subseteq B\) for some \(B\in D\); since \(D\) is a downset inside \(L_Q\), this forces \(A\in D\). Hence \(\Phi\) is injective.

It is not surjective. Pick \(A\in L_P\setminus L_Q\). Its principal downset \(\downarrow_{L_P}A\) cannot equal \(\Phi(D)\) for any \(D\). If it did, the membership \(A\in\Phi(D)\) would give some \(B\in D\) with \(A\subseteq B\). But \(B\in D\subseteq\Phi(D)=\downarrow A\), so also \(B\subseteq A\). Thus \(A=B\in L_Q\), a contradiction. Therefore
\[
|\operatorname{Dw}^{+}(L_Q)|<|\operatorname{Dw}^{+}(L_P)|,
\]
which is the claimed strict monotonicity.

For the upper extremum, the antichain order is contained in every partial order on the same carrier. Its upset lattice is the Boolean lattice \(2^{[n]}\), so its canonical carrier has \(M_n-1\) elements: all Boolean-lattice downsets except the empty family. Strict monotonicity shows that every non-antichain has smaller carrier.

For the lower extremum, extend any finite poset \(P\) to a linear order \(C\). If \(P\) is not already a chain, this is a strict order refinement, so \(|\mathcal I(C)|<|\mathcal I(P)|\). The upset lattice of an \(n\)-element chain is itself a chain of \(n+1\) elements, which has exactly \(n+1\) nonempty downsets. This proves the lower bound and its equality case.

## Verification
A standalone exact replay enumerates every labeled poset on at most four points: \(1,3,19,219\) posets in sizes \(1,2,3,4\). For each poset it independently constructs the upset lattice and exhaustively enumerates all nonempty downsets.

It then checks all \(3064\) strict order-refinement pairs on those carriers, verifies the strict cardinal inequality, and explicitly replays the proof injection \(D\mapsto\downarrow D\) on \(26554\) source downsets. It also verifies the unique chain and antichain equality cases and recovers the complete labeled size distributions
\[
\begin{aligned}
n=3:&\quad 4^6,\ 6^6,\ 9^6,\ 19^1,\\
n=4:&\quad 5^{24},\ 7^{36},\ 9^6,\ 10^{48},\ 13^{24},\ 14^{24},\ 19^{12},\ 20^8,\ 26^{24},\ 49^{12},\ 167^1,
\end{aligned}
\]
where the exponent denotes the number of labeled posets producing that carrier size.

Running `python3 verify_order_refinement.py` prints:

```text
VERIFY_OK 63276 exact assertions; 242 labeled posets; 3064 strict refinements; 26554 injection images
```

The finite replay is not the all-\(n\) proof; the all-\(n\) argument is the explicit injection and strictness witness above.

## Relationship to prior work
Quadrellaro's 2021/2022 paper supplies the canonical representation \(\operatorname{Dw}^{+}(\operatorname{Up}(P))\), proves that it yields finite core-generated well-connected inquisitive algebras, and establishes the finite duality. The inspected paper does not compare carrier cardinalities under inclusion of frame orders; searches within the full text found no occurrences of “cardinality”, “refinement”, “Dedekind”, or “antichain”.

General poset literature uses the ideal lattice \(I(P)\) extensively, including De Loof--De Meyer--De Baets (2006), but targeted searches for order-extension monotonicity of the **iterated** ideal/downset count did not locate the strict theorem above. Candidate-specific semantic-index searches likewise returned only unrelated poset or antichain counting results.

The chain and antichain endpoint counts themselves are standard. The retained originality claim is the strict cross-frame monotonicity for the canonical inquisitive/dependence carrier and the resulting uniqueness of the two extremizers.

## Limitations
This result is purely about carrier size. It does not assert that \(\Phi\) preserves the inquisitive operations, nor does it classify which integers between the two endpoints occur as carrier sizes. The originality search cannot exclude uncatalogued order-theoretic folklore phrased only in terms of iterated ideal lattices.

## References
1. D. E. Quadrellaro, *On Intermediate Inquisitive and Dependence Logics: An Algebraic Study*, arXiv:2104.00981 (first posted 2 April 2021); *Annals of Pure and Applied Logic* 173 (2022), 103143. DOI: 10.1016/j.apal.2022.103143.
2. K. De Loof, H. De Meyer, B. De Baets, *Exploiting the Lattice of Ideals Representation of a Poset*, *Fundamenta Informaticae* 71 (2006), 309--321. DOI: 10.3233/FUN-2006-712-309.
