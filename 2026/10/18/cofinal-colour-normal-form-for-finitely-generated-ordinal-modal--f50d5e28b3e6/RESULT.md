# Cofinal-colour normal form for finitely generated ordinal modal algebras

## Finding
Let \(0<\alpha\) be an ordinal and let \(q\ge1\) subsets \(P_1,\ldots,P_q\subseteq\alpha\) generate a Boolean modal subalgebra \(\mathcal B\) of \(\mathcal P(\alpha)\) with \(\Diamond U=\{\xi<\alpha:\exists\eta\in U,\ \xi\le\eta}\). Color each world \(\xi\) by the vector \(v(\xi)\in\{0,1}^q\) of its memberships in the generators.

Set \(\beta_0=\alpha\). When \(\beta_j>0\), let \(C_j\) be the set of colors occurring cofinally in \([0,\beta_j)\); explicitly, \(c\in C_j\) exactly when for every \(\gamma<\beta_j\) there is \(\xi\) with \(\gamma\le\xi<\beta_j\) and \(v(\xi)=c\). Define
\[
\beta_{j+1}=\sup\{\xi+1:\xi<\beta_j,\ v(\xi)\notin C_j}\qquad(\sup\varnothing=0).
\]
This strictly decreases until \(\beta_h=0\), necessarily for some finite \(h\). Put \(L_j=[\beta_{j+1},\beta_j)\) and \(A_{j,c}=\{\xi\in L_j:v(\xi)=c}\). Then the **Boolean atoms of \(\mathcal B\)** are exactly the \(A_{j,c}\) with \(0\le j<h\) and \(c\in C_j\). In particular,
\[
\boxed{|\mathcal B|=2^{\sum_{0\le j<h}|C_j|}.}
\]
This gives a finite, valuation-sensitive normal form for the generated algebra on **every ordinal**.

## Assumptions and scope
The relation is the reflexive forward ordinal order \(\le\), not the strict order \(<\); \(\alpha\) is any nonzero set ordinal, finite or infinite. The Boolean operations and \(\Diamond\) are finitary, and the generator family is finite. Colors absent from a segment are not cofinal. The convention for cofinality above also covers successor ordinals (only the last point's color is cofinal). No claim is made about arbitrary partial orders or infinite generator families.

## Proof
**1. Finite termination and exact layers.** There are at most \(2^q\) colors. For every color \(c\notin C_j\), its positions in \([0,\beta_j)\) are bounded strictly below \(\beta_j\). Their finite union is bounded, so \(\beta_{j+1}<\beta_j\). If no such position exists, \(\beta_{j+1}=0\). Because ordinals admit no infinite strictly decreasing sequence indexed by the naturals, some finite \(h\) has \(\beta_h=0\). Every point of \(L_j\) has color in \(C_j\), since any other point \(\xi\) would satisfy \(\xi+1\le\beta_{j+1}\). Conversely, every color \(c\in C_j\) occurs cofinally in \(L_j\): its cofinality in \(\beta_j\) and \(\beta_{j+1}<\beta_j\) guarantee occurrences above every position of \(L_j\). Thus the displayed \(A_{j,c}\) are nonempty and form a finite partition of \(\alpha\).

**2. Every proposed atom is definable.** The original Boolean operations produce each full color class \(V_c=\{\xi<\alpha:v(\xi)=c}\). Initially the initial segment \([0,\beta_0)=\alpha\) is available. Suppose \(I_j=[0,\beta_j)\in\mathcal B\). Then the finite union \(U_j=I_j\cap\bigcup_{c\notin C_j}V_c\) belongs to \(\mathcal B\). Directly from ordinal reachability,
\[
\Diamond U_j=\bigcup_{\eta\in U_j}[0,\eta+1)=[0,\beta_{j+1})=I_{j+1}.
\]
By induction, each \(I_j\) and therefore each \(L_j=I_j\setminus I_{j+1}\) is definable. Intersecting with \(V_c\) defines \(A_{j,c}\).

**3. No further atoms can appear.** Let \(\mathcal D\) be the finite Boolean algebra of all unions of the \(A_{j,c}\). Every generator belongs to \(\mathcal D\). If a nonempty \(U\in\mathcal D\) is given, select the highest (largest ordinal) layer \(L_j\) meeting \(U\). Within this layer, \(U\) contains at least one complete color cell \(A_{j,c}\), which is cofinal in \(L_j\). Hence \(\Diamond U\) contains all of \(L_j\), all lower ordinal layers, and no higher ordinal layer. It is therefore \(I_j=[0,\beta_j)\in\mathcal D\). Also \(\Diamond\varnothing=\varnothing\). Thus \(\mathcal D\) is closed under the modal operator, and the generated algebra \(\mathcal B\subseteq\mathcal D\). Step 2 establishes the reverse containment. Therefore \(\mathcal B=\mathcal D\), whose atoms are exactly the stated cells, and the cardinality formula follows.

## Verification
The standalone program `ordinal_modal_verify.py` enumerates all possible valuation-color words on finite ordinals through size eight for one generator, through size five for two generators, and through size four for three generators. It independently generates the Boolean-modal closure of the original generators, then compares its cardinality against the predicted cofinal-layer atom count. The result is `ORDINAL_MODAL_COFINAL_LAYER_NORMAL_FORM_OK 6554` (6,554 complete finite instances). This check does not establish the infinite-ordinal case; that case is proved by ordinal descent and layer cofinality above.

For example, on \(\alpha=\omega\), an alternating two-color valuation makes both colors cofinal and gives exactly four algebra elements. On \(\alpha=\omega+1\), if the top world has color \(1\) and the worlds below it alternate colors, the singleton top layer and the two cofinal cells below give three atoms and exactly eight elements. This illustrates why the natural-number chain alone does not determine the ordinal result.

## Relationship to prior work
Agnew's 2026 theorem classifies local finiteness of complex algebras of transitive frames, and its Proposition 3.18 establishes local finiteness for finite products of ordinal chains. That work gives a qualitative finiteness guarantee, not the valuation-sensitive exact atom partition or cardinality above. General tuned-partition approaches supply related background, but the present proof identifies the minimal generated algebra explicitly on a single arbitrary ordinal chain. Earlier natural-number one-generator calculations are consistent special cases and are strictly narrower: infinite alternating tails on \(\omega+1\) exhibit a layer absent from the \(\omega\) analysis.

## Limitations
The count is attached to a specified finite generator family; it is not a count of all subalgebras or all valuations. The result is for reflexive ordinal frames, not higher Cartesian products, arbitrary well-founded partial orders, or strict accessibility. Existing general frame-partition arguments may contain comparable normal forms under different terminology; the literature comparison is not a historical-priority proof.

## References
Gabriel Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941, first publicly submitted June 1, 2026, especially Theorem 3.16 and Proposition 3.18. https://arxiv.org/abs/2606.02941
