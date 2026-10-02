# Independent audit — 2026-10-02

## Final claim

For every integer \(\ell\ge 3\) and every integer \(n\ge 2\ell-3\), the weak rainbow saturation number of the star \(S_\ell\) is exactly \(\operatorname{rwsat}(n,S_\ell)=\binom{\ell}{2}-1\).

**Disposition:** passed.

## Correctness — PASS

After applying Li--Ma--Xie's rainbow-recoloring lemma, the initial graph may be taken rainbow. Writing \(r=\ell-1\), with \(d(v)\) the initial degree and \(a(v)\) the number of already inserted incident edges, the submitted local criterion is exact: a current nonedge \(xy\) is forced to create a rainbow \(S_\ell\) for every injective coloring of inserted edges iff an endpoint has \(d\ge r\) or \(a\ge r-1\), or both endpoints have \(d=r-1\) and \(a\le r-2\). Sufficiency follows from the available distinct initial or inserted incident colors. Necessity follows by assigning the current and previous inserted edges injectively to suitable initial colors (the two endpoint initial-color sets are disjoint in a rainbow initial graph) and then to fresh colors, leaving fewer than \(r\) distinct incident colors at both endpoints. An independent exhaustive collision-pattern check reproduced the criterion for \(r=2,3,4\), checking 36, 144 and 400 endpoint states with no mismatch; this finite check is supplementary to the proof. For the lower bound, assuming \(m\le\binom{r+1}{2}-2\), partition the vertices into \(A=\{d\ge r\}\), \(B=\{d=r-1\}\), and \(C=\{d\le r-2\}\). Degree counting gives \(|A|\le r-2\) and \(|A|+|B|\le r+1\). Some vertex outside \(A\) must eventually become strong; the first such vertex lies in \(B\), must acquire \(r-1\) inserted neighbors inside \(A\cup B\), and hence forces \(q=|A|+|B|\ge r\). The cases \(q=r\) and \(q=r+1\) each force \(m\ge\binom{r+1}{2}-1\), a contradiction; \(r=2\) is handled directly. For the upper bound, start from a rainbow \(K_\ell-pq\) plus isolates. The \(\ell-2=r-1\) other core vertices are initially strong; insert \(pq\), use \(r-2=\ell-3\) isolates to accumulate \(r-1\) inserted edges at each of \(p,q\), and then promote every remaining isolate from already strong vertices. This needs exactly \(n-\ell\ge\ell-3\), namely \(n\ge2\ell-3\), and starts with \(\binom{\ell}{2}-1\) edges. The boundary \(\ell=3\) is included.

**Risk and boundary:** The theorem proves a sufficient host-size threshold, not its optimality below \(2\ell-3\). The endpoint-color necessity argument uses the justified rainbow-initial recoloring reduction; without that reduction the disjoint initial-color-set step would not apply verbatim.

## Originality — PASS

Bo--Lian--Liu's primary full text was inspected through Theorem 1.3 and the complete star proof. It proves the same numerical value only under the stated hypotheses \(\ell\ge6\) and \(n\ge3\ell^2\). Their proof contains substantial slack in its host-size hypothesis, but it neither states nor establishes the submitted all-\(\ell\) boundary \(n\ge2\ell-3\); in particular its displayed extremal family and promotion argument are not a direct proof of the boundary cases for all \(\ell\). The audited result instead gives an exact endpoint-state criterion and a different \(K_\ell-e\) propagation that works at \(2\ell-3\) and for \(\ell=3,4,5\). Li--Ma--Xie supplies the definition, general asymptotic framework, and the rainbow-recoloring lemma, but no exact star threshold. Resultary searches using star, weak-rainbow-saturation, threshold, endpoint-state, and linear-host aliases returned the audited record as the only exact linear-threshold match; nearby published findings concern \(C_4\) or Berge-star saturation, which have different targets or models. Accordingly, no checked prior statement or implication dominates the submitted theorem.

### Equivalent formulations

**Searches**
- Resultary semantic search: weak rainbow saturation numbers stars S_l exact threshold host order linear n
- Web literature search: weak rainbow saturation star 2l-3
- arXiv:2609.03823v1, Theorem 1.3 and Section 3

**Evidence**
- Bo--Lian--Liu study the identical parameter \(\operatorname{rwsat}(n,S_\ell)\), so their theorem is the decisive equivalent formulation to compare.
- Their Theorem 1.3 states \(\operatorname{rwsat}(n,S_\ell)=\binom{\ell}{2}-1\) for \(\ell\ge6\) and \(n\ge3\ell^2\), a strict subrange of the submitted claim.
- No checked source states the endpoint-state characterization or the full \(n\ge2\ell-3\), \(\ell\ge3\) theorem.

The prior star theorem is genuinely the same invariant and overlaps the claim, but its stated and proved domain does not equal the submitted domain. Ordinary weak saturation, rainbow saturation, cycle weak-rainbow saturation, and Berge-star saturation are not equivalent because their forcing objects or color quantifiers differ.

### Broader coverage

**Searches**
- arXiv:2401.11525v1 and DOI 10.1002/jgt.23211
- arXiv:2609.03823v1 full star section
- Resultary search for stronger/general weak rainbow star theorems

**Evidence**
- Li--Ma--Xie prove a general asymptotic framework and the rainbow-recoloring reduction but no exact star formula at a linear host threshold.
- Bo--Lian--Liu is the strongest direct exact-star source found; its theorem assumes \(\ell\ge6\) and \(n\ge3\ell^2\).
- The Bo--Lian--Liu proof uses a large-host reserve in its stated construction. Some numerical slack can be reduced, but the inspected text does not furnish a theorem covering every \(n\ge2\ell-3\) and every \(\ell\ge3\).

No checked broader theorem implies the full submitted statement. The new range includes all \(2\ell-3\le n<3\ell^2\) for \(\ell\ge6\) and all eligible hosts for \(\ell=3,4,5\).

### Exact database or table

**Searches**
- Resultary: weak rainbow saturation numbers stars S_l exact threshold host order linear n
- Resultary: weak rainbow saturation stars endpoint criterion strong borderline
- Published-finding aliases: rainbow star saturation linear threshold K_l-e

**Evidence**
- The direct Resultary match is the audited 2026-09-30 record itself.
- The closest earlier published SCOPE hits located in these searches concern weak rainbow saturation of C4 or Berge-hypergraph star saturation, not this star parameter.
- No earlier exact table or record with the submitted threshold was located.

The database search does not prove novelty by absence; it is combined with the direct primary-source implication comparison above. No exact prior database row independently covers the claim.

### Claim versus prior implication

**Searches**
- Bo--Lian--Liu, arXiv:2609.03823v1, Theorem 1.3 and Section 3 proof
- Li--Ma--Xie, arXiv:2401.11525v1, main results and Lemma 2.4
- Resultary stronger-coverage search

**Evidence**
- Bo--Lian--Liu imply the submitted value only on their overlap \(\ell\ge6,\ n\ge3\ell^2\); their theorem does not cover \(2\ell-3\le n<3\ell^2\) or \(\ell=3,4,5\).
- Li--Ma--Xie's recoloring lemma is used as an input, but their general bounds do not yield \(\binom{\ell}{2}-1\) at \(n=2\ell-3\).
- The submitted proof needs a new exact local forcing criterion and a boundary construction \(K_\ell-e\) plus isolates.

The submitted theorem is not a parameter renaming or special case of a stronger checked theorem. Although the 2026 star proof has slack and can be optimized in some host ranges, reaching the full boundary and the small-star cases is not a direct stated corollary of that source.

### Primary-source inspections

1. **Weak rainbow saturation numbers of paths, stars and cycles** — arXiv:2609.03823v1. Trigger: same parameter, target and eventual exact value. Material read: abstract, definitions, Theorems 1.1--1.3, the complete star proof in Section 3, and Remark 3.1. Assessment: partial coverage. Theorem 1.3 proves the exact value for \(\ell\ge6\) and \(n\ge3\ell^2\), not the submitted full boundary.
2. **Weak rainbow saturation numbers of graphs** — arXiv:2401.11525v1; doi:10.1002/jgt.23211. Trigger: foundational definition and possible general implication. Material read: definitions, main-result context, and Lemma 2.4 with proof. Assessment: background only for this exact threshold; Lemma 2.4 supplies the recoloring reduction.

**Checked sources**
- Bo, Lian and Liu, Weak rainbow saturation numbers of paths, stars and cycles, arXiv:2609.03823v1
- Li, Ma and Xie, Weak rainbow saturation numbers of graphs, arXiv:2401.11525v1 / Journal of Graph Theory 109 (2025)
- Resultary semantic search for weak-rainbow star exact thresholds and linear host ranges
- Published SCOPE weak-rainbow C4 record 2026/9/17/SCOPE001, checked as a different target
- Published SCOPE Berge-star record 2026/9/16/SCOPE012, checked as a different saturation model
- Broad web literature search through 2026-10-02 UTC for exact weak-rainbow star thresholds and 2l-3 aliases

**Residual risks**
- Best-of-knowledge priority assessment: the directly relevant September 2026 literature is recent enough that an unindexed independent refinement may exist.
- The threshold \(2\ell-3\) is not claimed optimal; small computations show the exact value sometimes holds below it.
- The prior star proof contains slack in its published large-host hypothesis; this was treated as a comparison risk rather than ignored, but no checked prior source establishes the full submitted boundary.

## Scientific value — PASS

The result addresses an active exact extremal parameter and closes the known exact star value down to the explicit linear boundary \(n\ge2\ell-3\), while also covering the previously omitted orders \(\ell=3,4,5\). The contribution is not only a numerical threshold change: the exact endpoint-state rule converts the universal color quantifier into a reusable local dynamical condition, and the \(K_\ell-e\) construction explains how promotion propagates at the boundary. These features are mathematically useful for the still-open below-threshold classification. The theorem does not claim the threshold is least.

**Risk and scope:** The sufficient threshold is not optimal in every small case, and some slack in the prior large-host proof can be reduced; the value here rests on the exact all-orders boundary theorem and structural local criterion rather than on the phrase 'quadratic to linear' alone.

## Verification scope

The analytic proof, not the finite computations, establishes the all-orders statement. The finite endpoint-state computation was independently reproduced for \(r=2,3,4\) as a consistency check. The threshold below \(2\ell-3\) is not classified here.
