---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

The Chair44 hierarchy phase gives a necessary arithmetic sieve for Euclidean stabilizers: each nontrivial proper cubic rotation is compatible only on a dense Haar-null 2-adic set of Hausdorff dimension one, every noncyclic point group forces an ordinary integral phase, and invariant random registered tilings are almost surely asymmetric.

## Correctness — PASS

Unique registered hierarchy gives the exact covariance equation \((I-R)\alpha=t\). Independently enumerating the 24 proper signed-permutation rotations confirms rank two for \(I-R\) at every nonidentity rotation; the inspected verifier further gives Smith invariant counts \((1,1):8\), \((1,2):12\), and \((2,2):3\), so each compatible set is an integral two-coordinate slice times one 2-adic coordinate. Its subgroup census verifies full stacked rank with 2-power third determinantal divisor for every noncyclic subgroup, forcing integral phase. Translation covariance under dense \(\mathbb Z^3\) then forces the phase pushforward of an invariant measure to be Haar.

**Checked sources.** Assigned RESULT.md at tree 56f50d7be7a52efb6dc118bfd3293b3679190568; artifacts/verify_cubic_phase.py blob fc08570f45ec9af605d1638e8bbb3fd18e0cf396; Tsiokos, arXiv:2609.19214

**Residual risks.** The proof relies on the source's registered unique hierarchy; the source is very recent, although its abstract explicitly states that unique infinite hierarchy and the order-24 symmetry bound.

## Originality — PASS

The source establishes registration, unique hierarchy and an order-24 symmetry bound, but the searched prior work did not state the individual 2-adic stabilizer equation as a phase sieve, the exact dimension-one exceptional set, the noncyclic-implies-integral conclusion, or the Haar generic-asymmetry consequence for Chair44.

### Equivalent formulations

The audited claim concerns stabilizers of individual Chair44 tilings, not global extended symmetry groups or merely existence of an adic factor.

### Broader coverage

Those broader frameworks do not determine the Smith forms or noncyclic subgroup intersections used here.

### Exact database or table

The standard cubic group catalogue supplies raw finite group data but not the tiling-phase theorem.

### Claim versus prior implication

The source hypotheses are ingredients, not a theorem already implying the final dimension and integral-phase conclusions without new arithmetic work.

**Checked sources.** https://arxiv.org/abs/2609.19214; https://arxiv.org/abs/1207.6237; https://doi.org/10.3934/dcds.2018036; https://doi.org/10.1007/s00454-022-00387-8; semantic published-results search

**Residual risks.** The Chair44 preprint is extremely recent, so unindexed parallel work remains possible. The full primary PDF was not retrievable through the available route in this run.

## Value — PASS

The theorem converts an open symmetry-classification question into a sharp arithmetic phase sieve, proves generic asymmetry in measure and category, and reduces any large/noncyclic stabilizer search to the zero-phase fiber. These are natural structural consequences of the hierarchy, not arbitrary parameter slices.

**Residual risks.** The sieve is necessary only and leaves the zero-phase stabilizer classification open.

## Limitations

- The phase condition is necessary, not sufficient for a symmetry.
- The zero-phase fiber is not classified and order 24 is not shown attainable.
- Hausdorff dimension is in the 2-adic phase space; the dense-G-delta conclusion is restricted to the primitive registered substitution hull.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
