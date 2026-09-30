# Independent Audit — 2026-09-29

**Record:** `2026/09/19/accelerated-filtration-entropy-growth--ce32733d844c`  
**Title:** Universal acceleration gives divergent filtration entropy on every infinite-dimensional affine algebra  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Disposition:** **REPAIRED**

## Three-axis assessment

- **Correctness — PASS:** The universal acceleration theorem is correct. From a standard generating filtration S_m with unbounded dimensions, one can choose a strictly increasing superadditive index sequence r_n so that dim S_{r_n}−dim S_{r_{n−1}}≥e^{n²}; V_n=S_{r_n} is then multiplicative, exhaustive and finite dimensional, with entropy limsup +∞. The converse for finite-dimensional algebras is definitional. The original k[x] example and linear-control argument are also mathematically correct.
- **Originality — REPAIRED:** The record requires narrowing because an earlier SCOPE record from the same day, `accelerated-filtration-entropy-growth-obstruction--f6a5a54dee7a`, already contains the stronger k[x] full entropy spectrum [0,∞] and the linear-control repair. Those components are therefore not a distinct contribution here. The surviving contribution is the genuinely broader universal acceleration theorem for every infinite-dimensional affine algebra, which was not found in the 2024 entropy paper, the motivating 2026 preprint, or targeted re-filtering searches.
- **Scientific value — PASS:** After removing the duplicate pieces, the universal theorem has clear value: it shows that unrestricted finite-dimensional filtrations can force divergent entropy on every infinite-dimensional affine algebra, so “entropy zero for every filtration” characterizes finite dimensionality. This sharply isolates how little intrinsic information unrestricted filtration entropy carries.

## Independent checks

- Reconstructed the recursive choice of r_n and verified that all superadditivity constraints involve only finitely many previous indices.
- Checked that unbounded monotone dim S_m lets each prescribed jump exceed e^{n²}.
- Verified V_iV_j⊆V_{i+j}, exhaustivity, and the quotient-entropy lower bound.
- Compared the package against the earlier same-day SCOPE obstruction record and removed the duplicated k[x] and linear-control novelty claims.

## Literature and evidence

- Schwarz–Sebandal, Growth functions of algebras and an application to Leavitt path algebras — Motivating 2026 paper with unrestricted filtration-growth implications challenged by accelerated filtrations.
- Bock et al., Algebraic Entropy of Path Algebras and Leavitt Path Algebras of Finite Graphs — 2024 defining paper explicitly emphasizes filtration dependence and proves only linear reindexing behavior.
- Earlier SCOPE record f6a5a54dee7a — Earlier same-day record already gives the full k[x] spectrum and linear-control repair, so those are removed from this record’s novelty claim.

## Limitations

- The repair deliberately drops novelty claims for the k[x] counterexample family and linear-control repair because an earlier SCOPE record already contains stronger versions.
- The universal acceleration statement is elementary and could exist in older re-filtering language; originality is to the best of targeted searches.
- The theorem is stated for affine algebras in the unital convention used by the motivating source.

**Independent-audit disposition:** repaired.
