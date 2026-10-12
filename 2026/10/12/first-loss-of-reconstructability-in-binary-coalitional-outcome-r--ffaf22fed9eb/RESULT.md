# First loss of reconstructability in binary coalitional outcome-range signatures

## Finding

Fix a finite set of labelled agents, each with **exactly two** individually labelled actions, and an outcome set \(O=\{0,1\}\). A deterministic one-step game form is a map \(f:\{0,1\}^k\to O\). For each coalition \(C\subseteq[k]\), retain **all its exact achievable outcome ranges**, but neither the action profiles producing them nor their multiplicities:
\[
\Sigma_C(f)=\left\{\left\{f(a_C,b_{[k]\setminus C}): b_{[k]\setminus C}\in\{0,1\}^{[k]\setminus C}\right\}:a_C\in\{0,1\}^C\right\}.
\]
Call \(\Sigma(f)=(\Sigma_C(f))_{C\subseteq[k]}\) the *full exact coalitional outcome-range signature*. The coalitions, agents and outcomes are labelled. Two forms are action-isomorphic if they differ by independently exchanging each agent's two action names.

**Theorem (sharp first failure and exact census).** The signature \(\Sigma\) determines the action-isomorphism class for \(k=1\) and \(k=2\), but not for \(k=3\). At \(k=3\), the \(256\) game forms have exactly **46** action-isomorphism classes and **41** distinct full signatures. Exactly **three** signatures fail to determine a unique class: two represent **two** classes each (12 labelled forms in each signature), and one represents **four** classes (32 labelled forms). The other 38 signatures each represent one class.

The failure persists even if agent permutations and outcome exchange are also allowed. For example, order the eight profiles by \(j=a_1+2a_2+4a_3\). The two forms
\[
(f(0),\ldots,f(7))=(0,0,0,1,0,1,1,0),\qquad
(g(0),\ldots,g(7))=(0,0,0,1,1,0,0,0)
\]
have **identical** \(\Sigma_C\) for every coalition, yet are not isomorphic even with those additional permutations.

## Assumptions and scope

This is a local, one-step statement about finite deterministic concurrent game forms with fixed action-set cardinality \(2\) for each agent and fixed labelled binary outcome set. It is *not* about standard upward-closed \(\alpha\)-effectivity, in which every superset of an attainable outcome range is admitted; the invariant here retains all exact ranges. It also does not retain their action-level multiplicities. In the enumeration, both constant forms and all nonsurjective forms are allowed. Relabelling actions is permitted independently by agent; all outcomes and agents remain labelled for the numerical census. The displayed witness is inequivalent under the larger group that also permutes agents or exchanges outcomes.

## Proof

**1. Faithfulness for at most two agents.** With one agent, \(\Sigma_{\{1\}}\) tells exactly which of the two singleton outcomes occur among the agent's actions; this determines the truth table up to exchanging the two actions. For two agents, regard \(f\) as a labelled \(2\times2\) Boolean matrix. A constant matrix is determined by its outcome singleton, and a matrix with one exceptional entry is determined by which outcome is exceptional. Among matrices with exactly two ones, there are three action-isomorphism types: both ones in one row, both in one column, or ones at opposite corners. Their singleton-coalition signatures differ: respectively one agent can force both singleton outcomes while the other sees only the full range; the roles reverse for the column case; and for the opposite-corner case both agents see only the full range. Therefore no two action-nonisomorphic matrices have the same full signature. The exact numbers of signatures are \(3\) for one agent and \(7\) for two.

**2. Explicit three-agent collision.** Encode outcome ranges by \(1\leftrightarrow\{0\}\), \(2\leftrightarrow\{1\}\) and \(3\leftrightarrow\{0,1\}\). Directly fixing actions and letting their complement vary gives, **for both** displayed game forms, the eight range families indexed by coalition bitmask \(0,1,\ldots,7\):
\[
\big(\{3\},\{3\},\{3\},\{1,3\},\{3\},\{1,3\},\{1,3\},\{1,2\}\big).
\]
Here each outer brace is a family of range codes, not a multiset. The two game forms have respectively three and two profiles with outcome \(1\). Independent action swaps, agent permutations and even outcome swaps preserve the number of ones up to replacing \(t\) by \(8-t\). Because \(3\notin\{2,6\}\), these two forms are not isomorphic under the enlarged relabelling group. This proves failure for three agents and sharpness of the agent threshold.

**3. Complete three-agent census.** Index the \(2^{2^k}\) Boolean tables by integers \(t\in\{0,\ldots,2^{2^k}-1\}\), with \(f_t(a)\) equal to bit \(j=\sum_i2^{i-1}a_i\) of \(t\). For each subset-mask \(C\), enumerate all fixed assignments \(c\) with \(c\mathbin{\&}\neg C=0\), and form the output-range bitmask
\[
 r_t(C,c)=\bigvee_{j:\,j\mathbin{\&}C=c}2^{f_t(j)}.
\]
Sorting and deduplicating the \(r_t(C,c)\) yields \(\Sigma_C(f_t)\). This is precisely the finite enumeration implemented, with assertions, in `verify.py`; it enumerates **all** \(256\) tables, not a sampled subset. For each table the orbit representative is the smallest integer among its \(2^k\) independently flipped tables, where flipping the action bitmask \(b\) replaces table bit \(j\) by original bit \(j\mathbin{\oplus}b\). For \(k=3\), the resulting exact partition has 41 signature classes and 46 action-isomorphism classes; the only non-singleton collections of orbits have multiplicities \(2,2,4\) and corresponding labelled-table family sizes \(12,12,32\). The analogous complete checks for \(k=1,2\) give coincident counts \(3=3\) and \(7=7\), respectively.

The **46** is also independently certified by Burnside's lemma. The group \((\mathbb Z/2\mathbb Z)^k\) acts on the \(2^k\) profiles by translation. The identity fixes \(2^{2^k}\) Boolean tables; each nonidentity translation has \(2^{k-1}\) two-cycles and thus fixes \(2^{2^{k-1}}\) tables. Hence the number of action-isomorphism classes is
\[
 \frac{2^{2^k}+(2^k-1)2^{2^{k-1}}}{2^k},
\]
which equals \(3,7,46\) at \(k=1,2,3\), agreeing with the independent finite enumeration. The 41-signature and three-collision counts are established by the exhaustive finite checker and its fully displayed finite domain and range-generating rule.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter from the directory containing this document and `verify.py`. The verifier is standalone, uses only the Python standard library, enumerates the \(4+16+256\) truth tables for \(k\in\{1,2,3\}\), independently constructs every coalition range family, canonicalizes all action-flip orbits, checks the 41/46/3 census with multiplicities \(2,2,4\), checks the explicit collision and Hamming-weight obstruction, and checks Burnside's independent orbit counts. Its required final line is `PASS: first nonfaithfulness at three players; witness and exact census verified`.

The counts are exhaustive **only for the explicitly finite domain** \(k\le3\), two actions per agent, and two outcomes. The statement makes no extrapolation to arbitrary action or outcome cardinalities.

## Relationship to prior work

Ciardelli's *Inquisitive Action Logic* (2026), Section 2 and Theorem 2.2, defines individual-agent actual-effectivity families and proves an **existence/representability** characterization using nonemptiness, common ranges and independence; its introduction and conclusion explicitly distinguish the unresolved extension to proper coalitions. That theorem neither reconstructs a particular concrete outcome table from its *full* exact coalitional families nor counts possible collisions in a fixed binary action domain. The present theorem investigates this different faithfulness question, not a general solution to Ciardelli's coalition-representability problem.

Goranko and Jamroga's *State and path coalition effectivity models of concurrent multi-player games* develops state/path coalition effectivity and represents **upward-closed** strategy powers; this is a strictly coarser invariant, so its nonuniqueness or representation results do not entail the 41-versus-46 exact-range enumeration. The Stanford Encyclopedia of Philosophy survey *Reasoning About Power in Games* likewise explains established nonfaithfulness of conventional monotone coalitional power and distinguishes basic/nonmonotonic power. The present result does **not** claim that nonuniqueness of abstract game representations is new; its new candidate content is the sharp exact-range threshold and full small-domain census.

Wang's *Value Coalition Logic* (2026) introduces coalition-level value-range hypergraphs very close to the object \(\Sigma_C\). The available abstract does not state the minimal nonfaithfulness threshold or this enumeration; however, its full text was not available for material comparison, so potential equivalent coverage remains a substantive residual originality risk.

## Limitations

The theorem is a self-contained, precisely limited fixed-alphabet classification. It does not solve the existence problem for arbitrary prescribed coalitional effectivity families; it does not assert optimal action complexity; and it does not quantify collisions for four or more agents. The numerical 41, 46, 12 and 32 are justified by a short complete finite enumeration rather than a hand-derived generating function. The complete text of the closely related 2026 *Value Coalition Logic* preprint and any older equivalent Boolean-cube classification could in principle contain an equivalent result; the searches below are not proof of publication novelty. Independent validation has not been performed.

## References

- I. Ciardelli, *Inquisitive Action Logic*, Electronic Proceedings in Theoretical Computer Science **447** (2026), 222–241, doi:10.4204/EPTCS.447.13; first public arXiv record 2026-06-30, arXiv:2606.31866. Full text: https://www.researchgate.net/publication/408180960_Inquisitive_Action_Logic (Sections 2, 6, 7 and Appendix inspected).
- V. Goranko and W. Jamroga, *State and path coalition effectivity models of concurrent multi-player games*, *Autonomous Agents and Multi-Agent Systems* **30** (2016), 446–485, first published 2015, doi:10.1007/s10458-015-9294-4. Full HTML: https://link.springer.com/article/10.1007/s10458-015-9294-4 (definitions, representation results and discussion inspected).
- *Reasoning About Power in Games*, Stanford Encyclopedia of Philosophy, first published 2017, revised 2023, https://plato.stanford.edu/entries/logic-power-games/ (sections on coalition effectivity, basic power and nonmonotonic action logics inspected).
- S. Wang, *Value Coalition Logic: A Typed Assignment-Based Reconstruction of Coalition Logic*, arXiv:2605.25545, first public 2026-05-25, https://arxiv.org/abs/2605.25545 (abstract and indexed research description only; full text not inspected).
