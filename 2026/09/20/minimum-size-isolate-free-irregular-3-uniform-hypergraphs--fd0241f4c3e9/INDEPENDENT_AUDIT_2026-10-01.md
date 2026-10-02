# Independent scientific audit — 2026-10-01

Record: `SCOPE-20260920-fd0241f4c3e9`

Disposition: **passed**

The claim in `RESULT.md` is accepted unchanged. This audit assesses one final claim and requires separate correctness, originality, and scientific-value passes.

## Correctness — PASS

Distinct positive degrees on \(n\) vertices force degree sum at least \(1+\cdots+n\), so \(3m\ge n(n+1)/2\) and the stated ceiling is unavoidable. The base six-vertex seven-edge hypergraph has degrees \(1,\ldots,6\). In the inductive step, adding a new vertex \(x\) and triples \(xuv\) indexed by a simple link graph \(F\) preserves simplicity. In residue classes \(0,3\), a perfect matching increments exactly the old degrees \(k,\ldots,n-1\); in classes \(2,5\), it increments \(k,\ldots,n-3\); in classes \(1,4\), a three-edge path through the two largest old-degree vertices plus a matching increments the middle block by one and the top pair by two. The link has exactly \(M_n-M_{n-1}\) edges in every case, yielding precisely the claimed target degree set. I independently regenerated the abstract degree-multiset recurrence through \(n=100\); it matches the target in every residue class. The finite package verifier through \(n=200\) is therefore corroborative, not the proof.

The package computations, where present, were treated as supporting checks rather than substitutes for the general proof.

## Originality — PASS

### Equivalent formulations

**Searches/source IDs**
- Published SCOPE archive query: irregular 3-uniform hypergraph minimum edges isolate-free distinct degrees
- Published SCOPE archive query: irregular uniform hypergraph degree set 1 2 n minimum size
- Gyárfás et al. 1992 full text

**Evidence**
- The published SCOPE search returned no separate exact minimum-size match.
- The 1992 paper's Section 3 studies existence of irregular uniform hypergraphs, starting from the same six-vertex seven-edge example.

**Reasoning**

Existence and irregularity strength are not equivalent to minimizing the number of triples subject to no isolated vertices.

### Broader coverage

**Searches/source IDs**
- Gyárfás--Jacobson--Kinch--Lehel--Schelp 1992 full text
- Behrens et al. 2013 degree-sequence literature
- Li--Miklós arXiv:2312.00555

**Evidence**
- The 1992 induction may introduce an isolate and suggests removing it by adding \(n-1\) edges, without optimizing edge count.
- Later degree-sequence results address realizability/sufficient conditions, including dense regimes, rather than this sparse exact extremum.

**Reasoning**

These sources provide broader existence/realizability context but no statement that implies sharp attainment of the elementary degree-sum lower bound for every \(n\).

### Exact database or table

**Searches/source IDs**
- Published SCOPE semantic search for isolate-free irregular 3-graphs and the formula \(\lceil n(n+1)/6\rceil\)

**Evidence**
- No exact database/table of these minima was located.

**Reasoning**

The theorem is infinite and constructive; finite degree-sequence tables would not substitute for the induction.

### Claim versus prior implication

**Searches/source IDs**
- 1992 Theorem 3.3 and Proposition 3.1 discussion of isolated vertices
- arXiv:2312.00555

**Evidence**
- The classical theorem proves existence for \(r\ge3,n\ge r+3\), and explicitly notes an isolate may occur and can be removed by adding \(n-1\) edges.
- The dense realizability work is in a different parameter regime.

**Reasoning**

The prior existence construction does not imply the minimum-edge count; the audited link-graph induction is the substantive new sharpness argument.


### Source inspections

- **Irregularity Strength of Uniform Hypergraphs** — `https://users.renyi.hu/~gyarfas/Cikkek/61_GyarfasJacobsonKinchLehelSchelp_IrregularityStrengthOfUniformHypergraphs.pdf`. Trigger: Classical primary source for irregular uniform-hypergraph existence. Material read: Full open PDF, especially Section 3, Proposition 3.1 and Theorem 3.3. Method: Lawful open-access PDF. Assessment: NOT_COVERING the minimum-size isolate-free theorem. Evidence: Theorem 3.3 proves existence; the following note says the inductive construction may contain one isolate and proposes adding \(n-1\) new edges to remove it.

### Checked sources

- Gyárfás et al. 1992 full text
- DOI:10.37236/3414
- arXiv:2312.00555
- published SCOPE archive search

### Residual originality risks

- Older sparse 3-graphic sequence or irregular set-system literature may contain an equivalent edge-minimization result under different terminology.

## Scientific value — PASS

This determines the exact sparsest isolate-free irregular triple system at every admissible order and explains the precise modulo-six correction. It is a natural extremal refinement of the classical existence problem, with an explicit recursive construction rather than a finite census.

## Limitations

The theorem requires isolate-free simple 3-uniform hypergraphs, does not classify all extremal realizations, and does not address general uniformity. Older sparse degree-sequence/set-system literature remains a residual originality risk.

## Final assessment

Correctness: **PASS**  
Originality: **PASS**  
Scientific value: **PASS**  
Disposition: **passed**
