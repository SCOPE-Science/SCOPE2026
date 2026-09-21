# same-model review

Date: 16 September 2026. This is a same-model review. It is not independent validation.

**Overall: PASS under TBOK-v1.** Correctness: PASS. Value: PASS. Originality: PASS to the best of our knowledge, subject to the access limitations below. This is not a guarantee of first discovery.

## Exact claim reviewed

For every t >= 3, q >= 4t, and n >= q+2t+1, let H=K1 join (tK2 union qK1). Then sat(n,H)=n+3t-4, and the unique extremal graph is K1 join ((t-1)K3 union (n-3t+2)K1). Ordinary, not induced, containment is used. No conclusion for q<4t is asserted.

## Correctness: PASS

The argument in RESULT.md establishes both inequalities and the equality characterization for the entire quantified domain. It does not rely on computations for the lower bound.

The main skeptical checks were:

- A new H-copy must use the added edge. Its hub had original degree at least D=q+2t-1, regardless of whether the hub is an endpoint of that edge.
- An edge outside every triangle in H must be a pendant edge incident to its hub. This fact, not an assumed diameter-two property, is used whenever leaves or isolates are involved.
- The minimum-degree argument includes disconnected graphs and excludes isolated vertices. A complete saturated graph is impossible because n >= |V(H)|.
- The assertion that leaves have a common neighbour has an exception for adjacent leaves. The proof treats that exception explicitly: an isolated K2 forces exactly two leaves, and the edge budget bounds every other vertex's degree below D, contradicting saturation across components.
- With l leaves at v, the degree estimate for x outside the leaves and v is 2m >= l+l+d(x)+2(n-l-2)=2n+d(x)-4. Hence d(x)<=6t-4<D, and any vertex outside N[v] creates the required contradiction. This is the decisive structural step.
- Once v is universal, R=G-v has at most 3t-3 edges on at least 6t vertices, so R has an isolate. The reduction to matching saturation checks that in G+xy no other vertex can have the hub's required degree. Padding a matching with q vertices is legitimate because n-1>=2t+q; extra edges do not matter for ordinary subgraphs.
- The Tutte--Berge proof of the matching lemma handles arbitrary components. An isolate cannot belong to a maximum-deficiency barrier. A nonempty barrier contradicts saturation by adding an edge from the isolate to the barrier. With the empty barrier, missing internal component edges and edges from an even component to an isolate cannot increase matching number. Thus all components are odd cliques, and equality in a(2a+1)>=3a forces triangles and isolates.
- The construction's missing edges always join different base components. A triangle can avoid the at-most-one endpoint it contains, so t disjoint petal edges really are obtained after every addition. The count of remaining vertices is sufficient at the boundary n=q+2t+1.

`artifacts/verify_pendant_fans.py` ran successfully using the standard library. There were 10,440 agreements between recursive neighbourhood matching and a generic injective graph-embedding checker. Exhaustive enumeration of all 32,768 labeled graphs on six vertices produced sat(6,H_{2,1})=8, equal to HP26's formula, and 60 labeled minimizers of one isomorphism type, equal to its construction. Sixteen constructions in the new range passed their edge-count/freeness checks and all 6,472 missing-edge additions; 700 additions also passed the independent generic checker. Small positive and negative controls passed. These finite tests are supporting checks, not a substitute for proof.

An initial optional NetworkX installation failed its integrity check; no result relies on it. The final script has no external dependencies. Exploratory random-saturation output from the earlier session is not used to certify any minimum.

## Value: PASS

HP26 Theorem 1.4 gives the two-petal case, and Section 6, Problem 3 asks for all t>=3 and q>=1. The result resolves every q>=4t, for every t>=3 and every admissible n in that range, and characterizes all extremizers. It also gives an explicit connectedness result for matching bases, relevant to the broader question in HP26 Section 6.

The advance is modest but substantive: it proves the exact additive constant and uniqueness where the available general framework supplies only n+O(1) and an upper construction. The proof is short and elementary except for a standard matching theorem. Shortness is not itself novelty: the construction, matching classification, and cone reduction are credited as known. The residual is the universal-vertex forcing argument with pendant edges, which requires excluding new-edge embeddings as pendant edges rather than importing the existing triangle/diameter proof. The range restriction is tied to this degree argument, not an arbitrary computed subclass. No sharp threshold or all-q resolution is claimed.

## Originality: PASS to the best of our knowledge

### Equivalence and stronger-coverage checks

The target was translated to a friendship/fan/Dutch windmill graph with leaves at its centre; a cone over a matching with isolates; and equality, with uniqueness, in the standard cone saturation inequality. The auxiliary isolates can be eliminated from the **base** saturation number for n-1>=2t+q. They cannot be eliminated from the **joined forbidden graph**, where they are pendant vertices. This prevents a misleading reduction to the already solved fan problem.

The closest general result applying to the containing class is Cameron--Puleo, arXiv:2004.05410v2, Section 2 Lemmas 4--5 and Section 3 Lemmas 6--7. Substituting the exact weight 3 into their explicit Lemma 4 proof gives n-1; Lemmas 5--7 give the upper construction and n+O(1), not the positive additive term 3t-4 or uniqueness. Their proof retains this gap. This is an explicit parameter substitution, not a conclusion from different terminology.

The closest exact join result is Hu--Luo--Peng, quoted in HP26 Theorem 1.1: it requires a base without isolates. The closest accessible structural proof is Zhang et al., arXiv:2510.10458v1, Section 4, proof of Theorem 1.3. Its abstract and Section 4 require no isolates, despite an inconsistent sentence in the introduction saying "with isolated vertices". Inspection of Claim 1 shows exactly where non-isolation is needed: the claim that any new hub-to-base edge completes a triangle. A pendant edge violates that inference. Following the rest of that proof therefore does not establish the needed universal vertex. RESULT.md Step 2 supplies the missing step.

Fuller--Gould, Section 2 Theorem 3, covers standard generalized friendship graphs formed from equal-size cliques intersecting on a common clique; Lemmas 4--6 cover fans without the pendant extension. Their diameter-two proof does not transfer. Zhou--Kamiyama, Theorems 2--4 and Section 3, concerns disjoint triangles and quotes the older matching classification. The latter is deliberately treated as a known ingredient, not a finding.

The starting HP26 source explicitly establishes t=2 and poses t>=3 as Problem 3. Its open-problem status alone was not used as proof of novelty: the general cone proofs and the equivalent formulations above were checked separately. No accessible theorem, specialization, or followed proof was found to establish the new Step 2. The unread generalized-friendship source is discussed separately below rather than being declared non-covering.

### Evidence record

Searches covered the exact paper identity, generalized friendship graphs, pendant edges, joins of matching and isolates, covering theorems, universal vertices, windmills and equivalent joins. Some searches did not return usable results; those failures are not novelty evidence. Search snippets were used to identify sources and access concerns, not to prove absence of coverage.

Primary text inspected and used:

- HP26, retrieval: introduction/Theorems 1.1--1.4, Section 5 proof, Section 6 Problems 1--3; current reads 0--14500, 21800--28300, and references 31300--end, supplementing earlier reads.
- Zhang et al., retrieval: introduction including the inconsistent scope sentence; complete Section 4 argument at 34170--38670; references at 40500--44100.
- Fuller--Gould, retrieval: Section 2 Theorem 3, Lemmas 4--6 and beginning of Section 3, current read 3000--9500, supplementing earlier reads.
- Cameron--Puleo, retrieval, arXiv v2: Section 2 and Section 3 at 0--17400; delivered page 9 also displays Corollary 11 with clique orders at least two.
- Zhou--Kamiyama, retrieval, arXiv v1: 0--12500, containing main theorem statements and Section 3's matching result and disjoint-triangle construction.

No claim is made to have read every page of every cited source. Quoted older results and inaccessible originals are distinguished.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

The following sources were not obtained through available channels. The classification is ACCESS_LIMITATION, never NOT_COVERING.

1. **Jinze Hu, Shengjin Ji, Chenke Zhang (2025), _Some results on the saturation number of graphs_, DOI 10.1016/j.dam.2025.04.038.** Highest concern: the abstract treats relationships between saturation for disjoint clique unions and generalized friendship graphs. This could cover the target if singleton cliques are allowed under its operative theorem. Full-text acquisition was unsuccessful; the accessible abstract supplies only a relevance clue. The actual singleton-clique hypotheses and proof remain unverified. The abstract asserts results for some generalized friendship graphs without specifying our parameters or pendant extensions. Thus there is a meaningful possible threat, but no located concrete statement that covers the exact claim. HP26's current explicit Problem 3 and statement that existing join results exclude isolates provide corroborating context, not proof about the unread original. Under TBOK-v1 this limits, rather than automatically defeats, the assessment.
2. **S. Hu, Z. Luo, Y. Peng (2024), _Saturation numbers of joins of graphs_, DOI 10.1016/j.dam.2024.06.024.** Failed retrieval. General join equality is a plausible threat, but its precise theorem as quoted in two accessible sources excludes isolates. Further proof consequences in the original remain unverified; no concrete covering extension was identified.
3. **Zhang, Lu and Yu (2024), _A note on the minimum size of matching-saturated graphs_, DOI 10.1016/j.dam.2024.01.017; L. Kaszonyi and Z. Tuza (1986), _Saturated graphs with minimal number of edges_, DOI 10.1002/jgt.3190100209.** Both full texts were unavailable. These are relevant to the matching classification and cone tools, which are expressly not claimed as original. Their possible further structural consequences remain unverified. Accessible attributions were inspected and a Tutte--Berge proof was supplied; no concrete covering claim for the pendant-fan theorem was found.

A later covering theorem would require revision of this assessment. The PASS is a documented same-model assessment within this scope, not independent confirmation or an exhaustive literature certificate.

## Recorded review qualifications

> **Review status: same-model review.** Same-model review: passed. Independent audit: not yet performed. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.

## Recorded review qualifications

Same-model review:passed. Independent audit: not yet performed.
