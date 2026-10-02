---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For continuous \(\varphi:(0,\infty)\to\mathbb R\), the planar Delaunay triangulation universally maximizes \(\sum_\Delta\varphi(r_\Delta)\) exactly for affine \(\varphi(t)=at+b\) with \(a\ge0\), and universally minimizes it exactly for affine \(\varphi\) with \(a\le0\); equivalently, separable inradius invariance on every cyclic quadrilateral forces affinity.

## Correctness — PASS

One-sided perturbations of a cyclic quadrilateral force exact equality of the two separable inradius sums at the cyclic limit. The explicit cyclic kite has diagonal inradii \(u,u\) versus \(u(1+\delta),u(1-\delta)\), with arbitrary \(u>0\) and \(-1<\delta<1\), so the equality is precisely the midpoint Jensen equation; continuity forces \(\varphi\) affine. A concrete noncyclic quadrilateral fixes the slope sign, and Lambert's linear mean-inradius theorem supplies the converse. The inspected kite verifier checks the coordinate formulas and near-cyclic power examples but is only corroborative.

**Checked sources.** Assigned RESULT.md and artifacts/verify_kite.py at the frozen source tree; Timothy Lambert, The Delaunay Triangulation Maximizes the Mean Inradius, 1994 abstract/proceedings metadata; Minculete--Barbu--Szöllősy, About the Japanese Theorem, 2012; classical Japanese theorem summaries

**Residual risks.** No correctness defect was found.

## Originality — PASS

The classical sources establish linear inradius-sum invariance on cyclic polygons and Lambert's linear Delaunay optimality, but the searched literature and published-result corpus did not reveal the functional classification saying that every continuous unweighted separable transform with universal Delaunay extremality must be affine. The full Lambert paper remains the closest inaccessible source and is retained as a concrete best-of-knowledge risk.

### Equivalent formulations

The cyclic-invariance formulation and universal-Delaunay-extremality formulation are equivalent in the audit through the two-sided perturbation argument; no prior source inspected states the resulting midpoint-Jensen classification.

### Broader coverage

These broader results do not dominate an unweighted separable inradius classification.

### Exact database or table

A finite table is inapplicable because the claim classifies a continuum of continuous functions.

### Claim versus prior implication

The final classification is not a mechanical corollary of the linear theorem alone.

**Checked sources.** Lambert 1994; Minculete--Barbu--Szöllősy 2012; Klyachin--Grigorieva 2017; published mathematical corpus search

**Residual risks.** The full Lambert paper was unavailable, and equivalent folklore under classical Japanese-theorem language remains possible.

## Value — PASS

The theorem classifies an entire natural family of Delaunay objectives, explains the rigidity of the classical linear criterion, and supplies systematic near-cyclic counterexamples for every nonlinear power. This is a motivated structural classification rather than a single numerical refinement.

**Checked sources.** Lambert 1994 linear criterion; Japanese-theorem literature; general Delaunay-functional literature

**Residual risks.** Its proof is short once the cyclic kite is identified, but the classified function family and sharp universal boundary are natural objects of study.

## Limitations

- Continuity of the scalar transform is assumed.
- Only ordinary Euclidean planar triangulations of finite point sets are treated.
- No constrained, weighted, surface, or higher-dimensional analogue is claimed.
- The full text of Lambert's 1994 proceedings paper could not be obtained through available lawful access; its abstract and later theorem summaries were inspected.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
