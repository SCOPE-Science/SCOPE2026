# Independent mathematical audit

## correctness

PASS

On each selected cell (i,j), the external-neighbor count is (n−ρ_i)+(m−κ_j), yielding ρ_i+κ_j≥m+n−k. Every dominating set covers every row or every column: simultaneous empty row and column would leave their intersection undominated. In the all-rows case the occupied rows satisfy ρ_i≥max(1,n−k), so |D|≥m max(1,n−k); similarly all-columns gives |D|≥n max(1,m−k). Full parallel strips attain both bounds at their respective sizes. For 1≤k<min(m,n), equality forces every used column or row to be completely full, classifying all minimizers and giving binomial counts. k=0 gives D=V by graph connectedness; at k=m+n−2 ordinary domination gives min(m,n). A freshly written exact subset checker enumerated 124,742 nonempty subsets across 58 m≤n capacity instances with no discrepancies, independently of the submitted program. These finite checks support, but cannot prove, the infinite theorem.

## originality

PASS

The June 2026 full first version of Tepeh, arXiv:2606.22428, proves only a Cartesian-product upper bound (Theorem 7) and square diagonal equality for K_{k+2} □ K_{k+2} (Proposition 8). Neither implies the all-(m,n,k) matching lower bound nor the complete low-capacity optimizer classification. The September 2026 open-access originating paper establishes definitions and equivalent (1,t) parameters but no rook-product formula. Searches of published mathematical results for these claims and aliases returned no stronger covering theorem. A revised October 2026 v2 abstract exists, but its full body could not be inspected; originality is assessed at best knowledge with that substantive risk.

## value

PASS

Rook graphs are the canonical two-factor Cartesian products isolated by Tepeh as sharpness witnesses. Showing that the existing general product upper bound is attained for every rectangular pair and every capacity settles a natural exact invariant over a full infinite three-parameter family, and the low-capacity equality case classifies and counts all optimizers. The row/column saturation obstruction provides reusable structure beyond numerical examples. The theorem neither claims all higher Cartesian products nor classifies high-capacity optima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
