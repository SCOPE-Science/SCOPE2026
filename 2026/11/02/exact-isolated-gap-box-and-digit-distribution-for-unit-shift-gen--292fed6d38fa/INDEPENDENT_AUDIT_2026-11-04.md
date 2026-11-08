# Independent mathematical audit

## correctness

PASS

Using the published Apéry representative theorem w(q)=q+m L_n(q), verified that canonical digit strings cover residues 0,...,m-1 without collision and heights concatenate as L_n=(L_{n-1}+0,...,L_{n-1}+b-1,b). Adjacent jumps are +1 or 1-b. Isolated gaps correspond exactly to internal peaks with left +1 and right 1-b; residue 0 and terminal residue fail separately. Peaks form the disjoint digit box q=b+sum_{i=3}^n d_i r_{i-1}, giving x=(b-1)m+b+sum d_i a_i and the claimed count, polynomial and extrema. Independently generated Apéry sets by residue-Dijkstra and enumerated all gaps in 16 parameter families, checking 64 exact assertions. This supports the universal structural proof but does not replace it.

## originality

PASS

Branco–Colaço–Ojeda 2021 prove the general canonical Apéry theorem and Frobenius formula, both attributed prior, but do not state the resulting isolated-gap box. Singh–Ram 2024 and Smith 2022 treat especially embedding-dimension-two cases, whereas this theorem requires n>=3. Full Smith text unavailable, so mathematical priority is qualified; no identified stronger result covers the full unit-shift all-n distribution.

## value

PASS

Isolated gaps and perfection are independently motivated semigroup invariants. The theorem completely classifies a natural infinite arithmetic family, encoding every gap without duplicates and giving an exact exponential cardinality and nontrivial height-stratum generating function; it is not merely the old Frobenius number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
