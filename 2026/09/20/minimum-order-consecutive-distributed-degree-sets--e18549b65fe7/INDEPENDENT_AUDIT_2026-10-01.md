# Independent scientific audit — 2026-10-01

Record: `SCOPE-20260920-e18549b65fe7`

Disposition: **passed**

The claim in `RESULT.md` is accepted unchanged. This audit assesses one final claim and requires separate correctness, originality, and scientific-value passes.

## Correctness — PASS

For part sizes \(x,y\), forcing degrees \(1,\ldots,b\) on the \(Y\)-side gives \(e\ge y+b(b-1)/2\), while forcing exactly the set \([a]\) on \(X\) gives \(e\le ax-a(a-1)/2\). The resulting order lower bound is strictly increasing in \(y\), so equality starts at \(y=b\) and yields the stated ceiling. At equality the proposed row sequence is the staircase \((a,\ldots,1)\) plus copies of \(a\) and one remainder; the column staircase \((b,\ldots,1)\) is self-conjugate and majorizes the row sequence after adjoining the common lower staircase, so Gale--Ryser gives a simple realization. The connected-realization lemma is valid: among realizations with the fewest components, \(e\ge n-1\) forces a cyclic component, and a degree-preserving cross-component 2-switch using a cycle edge reduces the component count. The sharp sequences satisfy \(e\ge n-1\) for every \(a\ge2\); for \(a=1<b\), every \(X\)-vertex has degree one, so two \(Y\)-vertices cannot be joined. The proof therefore covers all parameters, and the finite verifier is only supplementary.

The package computations, where present, were treated as supporting checks rather than substitutes for the general proof.

## Originality — PASS

### Equivalent formulations

**Searches/source IDs**
- Published SCOPE archive query: bipartite distributed degree sets unequal cardinality minimum order consecutive
- Published SCOPE archive query: distributed degree sets minimum order different cardinalities bipartite
- DOI:10.1515/ausi-2015-0013

**Evidence**
- The published SCOPE search returned no separate theorem equivalent to the displayed formula.
- Iványi--Pirzada--Dar quote Manoussakis--Patil that determining the minimum-order property for arbitrary positive sets of different cardinalities was open, then prove existence without a minimum-order claim.

**Reasoning**

Existence for arbitrary distributed degree sets is weaker than the exact minimum-order formula for \([a],[b]\), and equal-cardinality minimum-order results do not imply the unequal consecutive formula.

### Broader coverage

**Searches/source IDs**
- Iványi--Pirzada--Dar 2015 full text, Theorem 41 and Example 42
- Manoussakis--Patil 2014 minimum-order framework

**Evidence**
- Theorem 41 supplies arbitrary-cardinality existence; Example 42 gives the connected obstruction \(\{1\}\) versus \(\{1,2\}\), but no all-\(b\) minimum-order formula.
- The earlier minimum-order theorem is restricted to equal cardinalities.

**Reasoning**

The general existence theorem does not dominate a sharp optimization theorem; the connected classification for the consecutive family is additional.

### Exact database or table

**Searches/source IDs**
- Published SCOPE semantic search for distributed degree sets and minimum order

**Evidence**
- No table/database result encoding these minima was located.

**Reasoning**

The formula is derived symbolically from degree sums and Gale--Ryser rather than from finite tabulation.

### Claim versus prior implication

**Searches/source IDs**
- DOI:10.1515/ausi-2015-0013 full text around Theorem 41
- DOI:10.7151/dmgt.1742

**Evidence**
- The 2015 paper explicitly distinguishes the earlier minimum-order question from its subsequent existence theorem and notes that its general construction need not be minimum order.

**Reasoning**

No inspected prior statement mechanically yields the ceiling term or proves connected attainment at that same order.


### Source inspections

- **Tripartite graphs with given degree set** — `https://doi.org/10.1515/ausi-2015-0013`. Trigger: Primary follow-up addressing distributed degree sets of unequal cardinalities. Material read: Full text around the discussion of Manoussakis--Patil, Theorem 41, and Example 42. Method: Lawfully accessible full text. Assessment: NOT_COVERING the minimum-order theorem; it proves existence for arbitrary distributed degree sets and records a connected obstruction example. Evidence: The text states that the different-cardinality minimum-order problem was open before Theorem 41 and then proves existence, not optimal order.

### Checked sources

- DOI:10.1515/ausi-2015-0013
- DOI:10.7151/dmgt.1742
- DOI:10.1016/S1571-0653(04)00554-2
- Gale--Ryser classical criteria
- published SCOPE archive search

### Residual originality risks

- Older theses or differently indexed work on distributed score/degree sets could contain the consecutive-family formula.

## Scientific value — PASS

The result answers a previously identified unequal-cardinality minimum-order direction for the canonical consecutive family and additionally settles when the same optimum can be connected. It supplies an exact closed formula and a sharp infinite obstruction family rather than a routine recomputation.

## Limitations

The theorem treats consecutive positive distributed degree sets \([a]\) and \([b]\), not arbitrary unequal-cardinality sets; the equal-cardinality specialization is prior territory. Unindexed equivalent formulations remain possible.

## Final assessment

Correctness: **PASS**  
Originality: **PASS**  
Scientific value: **PASS**  
Disposition: **passed**
