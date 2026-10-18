# Exact semantic quotient and two-neighbourhood compression on finite intuitionistic chains

## Finding
Fix the labelled chain \(W_n=\{0<1<\cdots<n-1\}\), where \(n\ge1\), with the constructive neighbourhood interpretation of the two intuitionistic monotone modalities. Restrict to frames where every neighbourhood family is nonempty and every member of that family is nonempty (the customary sufficient frame conditions for the \(\mathsf N\) and \(\mathsf P\) axioms). Two such frames satisfy exactly the same formulas **at every world, under every persistent valuation** if and only if two explicitly defined suffix-minimum profiles agree.

Every class has a representative with **at most two neighbourhoods per world, each containing at most two points**; two neighbourhoods are sometimes necessary if \(n\ge2\). All possible profile pairs occur, and their exact number is
\[
\boxed{\binom{2n-1}{n}^{2}}.
\]
For \(n=1,2,3,4,5\) these numbers are \(1,9,100,1225,15876\), respectively.

## Assumptions and scope
A constructive neighbourhood frame is \(F=(W_n,\le,N)\), with the displayed total order and, for each \(i\in W_n\), a nonempty **set** \(N(i)\) of nonempty subsets of \(W_n\). Propositional letters may receive arbitrary upsets of the chain; at least one letter is available. The language consists of \(\bot,\wedge,\vee,\to,\Box,\Diamond\) with arbitrary nesting. Intuitionistic implication satisfies \(i\Vdash\varphi\to\psi\) exactly when every \(j\ge i\) forcing \(\varphi\) forces \(\psi\). The two modal clauses are
\[
 i\Vdash\Box\varphi\iff\forall j\ge i\ \exists A\in N(j)\ \forall u\in A\ (u\Vdash\varphi),
\]
\[
 i\Vdash\Diamond\varphi\iff\forall j\ge i\ \forall A\in N(j)\ \exists u\in A\ (u\Vdash\varphi).
\]
All these truth sets are upsets. No reflexivity or transitivity assumptions are placed on a separate modal relation: there is no such relation. No arbitrary neighbourhood is required to be an upset. The theorem concerns **pointwise semantic equivalence under every valuation**, not mere equality of globally valid formulas and not identification of frames up to relabelling.

For any nonempty finite \(A\subseteq W_n\), its \(\min A\) and \(\max A\) refer to chain indices. Define, for each world,
\[
 b_i=\max_{A\in N(i)}\min A,\qquad d_i=\min_{A\in N(i)}\max A,
\]
then define the observable profiles
\[
 B_i=\min_{j\ge i}b_j,\qquad D_i=\min_{j\ge i}d_j.
\]
Thus \(B,D\) are weakly increasing \(n\)-tuples with entries in \(\{0,\ldots,n-1\}\).

## Proof
**Step 1 (threshold-action lemma).** Every upset equals \(U_t=\{t,t+1,\ldots,n-1\}\) for a unique \(t\in\{0,\ldots,n\}\), where \(U_n=\varnothing\). For any nonempty set \(A\), one has \(A\subseteq U_t\iff\min A\ge t\) and \(A\cap U_t\ne\varnothing\iff\max A\ge t\). Substituting these two equivalences into the source's modal clauses yields, for every \(t\),
\[
 \llbracket\Box U_t\rrbracket_F=\{i:B_i\ge t\},\qquad
 \llbracket\Diamond U_t\rrbracket_F=\{i:D_i\ge t\}.
\]
These identities include \(t=0\) and \(t=n\). Because all local families and their members are nonempty, \(b_i,d_i\in W_n\), so the endpoints give the expected truth and falsity of the modalities on \(\top\) and \(\bot\).

**Step 2 (complete invariant).** If two frames have identical \(B,D\), Step 1 says their modal operations coincide on **every** upset. An induction on formulas gives equal truth sets: atomic sets and \(\bot\) agree under common valuations; the three propositional operations depend only on the common intuitionistic chain order; and the modal steps use Step 1. Conversely, if a coordinate \(B_i\) differs between two frames, let \(t\) be its larger value, assign a letter \(p\) the upset \(U_t\), and compare \(\Box p\) at world \(i\). The two truth values differ. A different coordinate \(D_i\) is separated similarly by \(\Diamond p\). Hence the invariant is necessary and sufficient for all formulas and all persistent valuations.

**Step 3 (realization and compression).** Let \(B,D\) be any independent weakly increasing \(n\)-tuples over \(W_n\). At world \(i\) define
\[
 N_*(i)=\begin{cases}
 \big\{\{B_i,D_i\}\big\},&B_i\le D_i,\\
 \big\{\{B_i\},\{D_i\}\big\},&B_i>D_i.
 \end{cases}
\]
When the endpoints are equal, the first family has one singleton member. In the first case the sole neighbourhood has minimum \(B_i\) and maximum \(D_i\). In the second case the largest of the two neighbourhood minima is \(B_i\), and the smallest of their maxima is \(D_i\). Thus the local extrema are exactly \(b_i=B_i,d_i=D_i\). Weak increase gives \(\min_{j\ge i} B_j=B_i\) and analogously for \(D\). So the frame realizes exactly the prescribed observable pair, while meeting the neighbourhood-size bounds. It validates the source's \(\mathsf N\) and \(\mathsf P\) conditions, and because every \(N_*(i)\) is nonempty it is also continual.

**Step 4 (optimality and enumeration).** For \(n\ge2\), choose any monotone profiles ending in \(B_{n-1}=n-1\), \(D_{n-1}=0\) (for example both constant). In any representative the terminal-world local extrema equal those observable terminal values. A family with one nonempty neighbourhood \(A\) would require \(\min A=n-1>0=\max A\), impossible. Therefore two neighbourhoods can be required at one world. When \(n=1\), only \(\{\{0\}\}\) is allowed, so one is optimal. Finally there are \(\binom{2n-1}{n}\) weakly increasing \(n\)-tuples drawn from an \(n\)-element set, by stars and bars. The two independently realizable coordinates give exactly the square of this number. This completes the proof.

## Verification
`verify_im_chain.py` uses the modal clauses directly, independently of the profile formula. It exhaustively enumerates all allowed neighbourhood frames for \(n=1,2\), checking every upset for both modalities and counting their semantic profile classes. It also constructs and independently checks one representative for **every** theoretically allowed pair of weakly increasing profiles for \(1\le n\le5\), and checks the sharp two-neighbourhood obstruction. Run with `python3 verify_im_chain.py`; no third-party modules are needed. The finite checks are supplementary; Steps 1–4 establish the unbounded theorem.

## Relationship to prior work
Dalmonte and de Groot (2026), Definition 2.3, Lemma 2.4 and its proof, introduce the constructive neighbourhood semantics and connect nonempty/nonempty-member conditions with the \(\mathsf N\), \(\mathsf P\) extensions. Their main results concern soundness, completeness, calculi and decidability, not an exact full-language semantic quotient, its count on labelled chains, or a two-neighbourhood representative. De Groot's earlier study (2025) develops a different, more general notion of intuitionistic neighbourhoods whose membership can vary with the order; its canonical semantics does not state this fixed-chain quotient. Earlier work on minimal and maximal neighbourhoods concerns different classes of intuitionistic systems. The arithmetic multiset count and min/max calculus are elementary ingredients; the contribution claimed here is their *complete combination* for the specific two-modal full-language semantic quotient, together with the sharp representative bound.

## Limitations
The conclusion is confined to **finite total orders** and to neighbourhood families that are nonempty and contain no empty neighbourhoods. Different underlying orders or other frame conditions may impose dependencies between the profiles. The quotient is with respect to all persistent valuations and formulas at labelled worlds; it does not classify isomorphism classes, unrestricted neighbourhood frames, or the alternative semantic structures with order-varying neighbourhood functions. The compression bound guarantees a representative, **not a unique or globally minimum-total-size representative**. Independent validation and exhaustive comparison with every historical synonym of neighbourhood equivalence have not been performed.

## References
1. J. de Groot, *Intuitionistic monotone modal logic via translation*, arXiv:2507.13746v1 (first public 18 July 2025); later Journal of Logic and Computation 36(4) (2026), DOI: 10.1093/logcom/exag017. https://arxiv.org/abs/2507.13746
2. T. Dalmonte and J. de Groot, *Intuitionistic Monotone Modal Logic: Proof Theory and Semantics*, arXiv:2606.31870v1 (30 June 2026), EPTCS 447 (2026), 278–298, DOI: 10.4204/EPTCS.447.16. https://arxiv.org/abs/2606.31870
3. T. Witczak, *Topological and Multi-Topological Frames in the Context of Intuitionistic Modal Logic*, Bulletin of the Section of Logic 48(3) (2019), 187–205, DOI: 10.18778/0138-0680.48.3.03 (distinct single-modality/topological approach).
