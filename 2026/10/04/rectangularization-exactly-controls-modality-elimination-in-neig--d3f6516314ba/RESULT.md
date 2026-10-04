# Rectangularization exactly controls modality elimination in neighborhood full products
## Finding

Let
\[
X=(X,\tau_1),\qquad Y=(Y,\tau_2)
\]
be normal neighborhood frames in the sense of Aghamov, Kudinov, Nguyen, and Piribauer: every \(\tau_i(z)\) is a filter, closed under supersets and finite intersections. Fix
\[
(x,y)\in X\times Y
\]
and abbreviate
\[
\mathcal F=\tau_1(x),\qquad \mathcal G=\tau_2(y).
\]
For \(P\subseteq X\times Y\), write its vertical section at \(u\in X\) as
\[
P_u=\{v\in Y:(u,v)\in P\}.
\]

The product modality \(\Box\) of the full neighborhood product and the iterated coordinate modality \(\Box_1\Box_2\) agree at \((x,y)\), for every valuation of a propositional variable, if and only if the pair \((\mathcal F,\mathcal G)\) has the following **rectangularization property**:

\[
\begin{aligned}
&Q\in\mathcal F\ \text{and}\ V_u\in\mathcal G\ \text{for every }u\in Q\\
&\qquad\Longrightarrow\quad
\exists U\in\mathcal F\ \exists V\in\mathcal G:\
U\subseteq Q\ \text{and}\ V\subseteq\bigcap_{u\in U}V_u.
\end{aligned}
\]

Equivalently, define two filters on \(X\times Y\):
\[
\mathcal R(\mathcal F,\mathcal G)
=
\{P:\exists U\in\mathcal F\ \exists V\in\mathcal G\ (U\times V\subseteq P)\}
\]
and
\[
\mathcal L(\mathcal F,\mathcal G)
=
\{P:\{u:P_u\in\mathcal G\}\in\mathcal F\}.
\]
Then always
\[
\mathcal R(\mathcal F,\mathcal G)\subseteq\mathcal L(\mathcal F,\mathcal G),
\]
which is the local set-theoretic content of the published interaction principle
\[
\Box p\to\Box_1\Box_2p.
\]
The reverse implication
\[
\Box_1\Box_2p\to\Box p
\]
is valid at \((x,y)\) for all valuations exactly when
\[
\mathcal L(\mathcal F,\mathcal G)=\mathcal R(\mathcal F,\mathcal G),
\]
and this equality is equivalent to rectangularization. Swapping the two factors gives the exact criterion for
\[
\Box_2\Box_1p\to\Box p.
\]

A finite collapse follows. If both factor frames are finite, every neighborhood filter is principal: for each point its total intersection is itself a neighborhood. Hence both rectangularization conditions hold, and every finite full product validates
\[
\Box p\leftrightarrow\Box_1\Box_2p
\qquad\text{and}\qquad
\Box p\leftrightarrow\Box_2\Box_1p.
\]
Thus on finite normal neighborhood full products the third modality is eliminable exactly as in full products of Kripke frames.

The finiteness phenomenon is sharp even for reflexive neighborhood frames. Let
\[
X=Y=\mathbb N.
\]
At every \(x\in X\), let
\[
\tau_1(x)=\{X\}.
\]
At every \(y\in Y\), let
\[
\tau_2(y)=\{V\subseteq Y:y\in V\ \text{and}\ Y\setminus V\ \text{is finite}\}.
\]
Both frames validate \(\mathsf T\). At \((0,0)\), put
\[
P=\{(u,v):v=0\ \text{or}\ v\ge u\}.
\]
Then
\[
\Box_1\Box_2p
\]
is true for the valuation \(\llbracket p\rrbracket=P\), while
\[
\Box p
\]
is false. Therefore the reverse interaction is genuinely an infinite compactness issue rather than a general law of neighborhood full products.

## Assumptions and scope

The neighborhood frames are normal filter frames as defined in the primary source. The theorem is local at a product point, so no reflexivity or seriality assumption is required for the rectangularization equivalence itself.

The finite corollary uses only finiteness of the underlying factor sets and the filter axioms. It does not assert that arbitrary finite non-normal neighborhood frames are relational.

The final counterexample uses \(\mathsf T\)-frames to show that reflexivity alone does not recover the reverse interaction in the infinite case.

The term “left Fubini filter” is used descriptively for \(\mathcal L(\mathcal F,\mathcal G)\); the theorem is proved directly from the modal semantics and does not depend on external filter-product theory.

## Proof

Let \(P\subseteq X\times Y\) be the truth set of a propositional variable.

By the definition of the product neighborhood function in a full product,
\[
(x,y)\models\Box p
\]
if and only if there are
\[
U\in\mathcal F,\qquad V\in\mathcal G
\]
such that
\[
U\times V\subseteq P.
\]
This is exactly
\[
P\in\mathcal R(\mathcal F,\mathcal G).
\]

For the iterated modality, define
\[
Q_P=\{u\in X:P_u\in\mathcal G\}.
\]
At a point \((u,y)\), the formula \(\Box_2p\) holds exactly when \(P_u\in\mathcal G\). Hence the truth set of \(\Box_2p\) along the horizontal fibre through \(y\) has first-coordinate set \(Q_P\). The horizontal clause gives
\[
(x,y)\models\Box_1\Box_2p
\quad\Longleftrightarrow\quad
Q_P\in\mathcal F.
\]
Thus
\[
(x,y)\models\Box_1\Box_2p
\quad\Longleftrightarrow\quad
P\in\mathcal L(\mathcal F,\mathcal G).
\]

If \(P\in\mathcal R(\mathcal F,\mathcal G)\), choose \(U\in\mathcal F\) and \(V\in\mathcal G\) with \(U\times V\subseteq P\). Then for every \(u\in U\),
\[
V\subseteq P_u,
\]
so upward closure of \(\mathcal G\) gives \(P_u\in\mathcal G\). Therefore
\[
U\subseteq Q_P,
\]
and upward closure of \(\mathcal F\) yields \(Q_P\in\mathcal F\). Hence
\[
\mathcal R\subseteq\mathcal L.
\]

Assume rectangularization. If \(P\in\mathcal L\), then
\[
Q_P\in\mathcal F.
\]
For each \(u\in Q_P\), take
\[
V_u=P_u\in\mathcal G.
\]
Rectangularization gives \(U\in\mathcal F\) and \(V\in\mathcal G\) with
\[
U\subseteq Q_P,
\qquad
V\subseteq\bigcap_{u\in U}P_u.
\]
Therefore
\[
U\times V\subseteq P,
\]
so \(P\in\mathcal R\). Thus
\[
\mathcal L=\mathcal R.
\]

Conversely, assume
\[
\mathcal L=\mathcal R.
\]
Let \(Q\in\mathcal F\) and choose \(V_u\in\mathcal G\) for each \(u\in Q\). Define
\[
P=\bigcup_{u\in Q}\bigl(\{u\}\times V_u\bigr).
\]
Then
\[
Q\subseteq\{u:P_u\in\mathcal G\},
\]
so \(P\in\mathcal L\). Equality gives \(P\in\mathcal R\), hence there are \(U_0\in\mathcal F\) and \(V\in\mathcal G\) with
\[
U_0\times V\subseteq P.
\]
Put
\[
U=U_0\cap Q.
\]
Because filters are closed under finite intersections,
\[
U\in\mathcal F.
\]
For each \(u\in U\), the inclusion \(U_0\times V\subseteq P\) gives
\[
V\subseteq P_u=V_u.
\]
Hence
\[
V\subseteq\bigcap_{u\in U}V_u,
\]
which is rectangularization.

Now suppose \(X\) and \(Y\) are finite. Since \(\mathcal F\) is a finite family closed under finite intersections,
\[
A=\bigcap\mathcal F
\]
belongs to \(\mathcal F\). Similarly,
\[
B=\bigcap\mathcal G\in\mathcal G.
\]
For any rectangularization instance, take
\[
U=A\cap Q\in\mathcal F
\]
and
\[
V=B.
\]
Because \(B\subseteq V_u\) for every \(u\), the required inclusion holds. The swapped argument is identical.

Finally consider the infinite \(\mathsf T\)-example. Every member of \(\tau_1(x)\) contains \(x\), and every member of \(\tau_2(y)\) contains \(y\), so both factors validate \(\mathsf T\). For each \(u\in\mathbb N\),
\[
V_u=\{0\}\cup\{v:v\ge u\}
\]
is cofinite, contains \(0\), and satisfies
\[
\{u\}\times V_u\subseteq P.
\]
Thus \(P_u\in\tau_2(0)\) for every \(u\), and therefore
\[
(0,0)\models\Box_1\Box_2p.
\]
If \((0,0)\models\Box p\), then because the only \(\tau_1(0)\)-neighborhood is all of \(\mathbb N\), there would be a cofinite \(V\ni0\) with
\[
\mathbb N\times V\subseteq P.
\]
Choose a positive \(v\in V\) and then \(u>v\). We have \(v\ne0\) and \(v<u\), so
\[
(u,v)\notin P,
\]
a contradiction.

## Verification

The bundled checker exhaustively enumerates principal filters on carriers of sizes through three in each coordinate and every subset of the corresponding product carrier. It verifies that the rectangle filter and both iterated filters coincide in every finite case.

The checker also evaluates finite truncations of the explicit infinite construction and verifies the section mechanism responsible for \(\Box_1\Box_2p\), while the general failure of \(\Box p\) is proved symbolically above from cofiniteness.

The finite computation is corroborative only. The arbitrary finite theorem follows from principality of finite filters, and the arbitrary-point characterization follows from the exact set identities above.

## Relationship to prior work

Aghamov, Kudinov, Nguyen, and Piribauer introduce the trimodal full product used here. Their product modality is generated by rectangles \(U\times V\), while the horizontal and vertical modalities are generated by one-coordinate fibres. They prove the forward interaction
\[
\Box p\to\Box_1\Box_2p\wedge\Box_2\Box_1p
\]
and establish exact logics for full products of \(\mathsf T\)- and \(\mathsf D\)-neighborhood frames.

The same paper contrasts this with full products of Kripke frames, where
\[
\Box p\leftrightarrow\Box_1\Box_2p
\]
is valid, and explicitly explains that its completeness construction needs genuinely non-Kripke neighborhood frames with no smallest neighborhood in order to falsify standard product interaction axioms.

Kudinov's earlier work on bimodal neighborhood products likewise uses filters without minimal neighborhoods to obtain behavior unavailable in Kripke products. That work does not contain the third product modality of the 2026 full-product semantics.

The present result identifies the exact local obstruction for the new third modality: rectangle-generated neighborhoods and iterated section neighborhoods coincide precisely under rectangularization. It then shows that all finite filter factors satisfy this automatically and supplies an explicit infinite reflexive failure of the reverse implication.

## Limitations

The exact characterization is pointwise. A frame validates the reverse implication globally exactly when the corresponding rectangularization condition holds at every product point.

The finite collapse does not extend to arbitrary infinite filters. The cofinite example shows failure even under \(\mathsf T\).

The result does not claim that rectangularization has no established formulation in abstract filter theory. The originality claim is restricted to the modal full-product characterization, the finite eliminability consequence, and the explicit reflexive boundary checked against the cited neighborhood-product literature.

## References

[1] Rajab Aghamov, Andrey Kudinov, Maik Thanh Nguyen, and Jakob Piribauer, “On Modal Logics of Full Products of Neighborhood Frames,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 1–15. DOI:10.4204/EPTCS.447.1. arXiv:2606.31852.

[2] Andrey Kudinov, “Neighbourhood frame product KxK,” *Advances in Modal Logic* 10 (2014).

[3] Eric Pacuit, *Neighborhood Semantics for Modal Logic*, Springer, 2017.
