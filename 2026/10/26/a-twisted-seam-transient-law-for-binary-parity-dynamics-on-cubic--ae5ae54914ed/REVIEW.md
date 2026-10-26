# Scientific review

## Correctness — PASS
The proof identifies the two update operators exactly, and establishes the only zero primary factor \(\Phi(z)=z^2+z+1\) by solving \(\lambda^n=1\) over characteristic two. On the Möbius graph the exact multiplicity is one for even \(n\) and two for odd \(n\), which gives sharp nilpotent indices. On the prism the matrix square and its two local Smith factors give different nilpotent indices despite equal stable-image dimension. The dimension/count arguments are valid for every integer \(n\ge3\). The separate bitset-rank and full-state finite tests reported in `verification_output.txt` agree, but do not substitute for the proof.

## Originality — PASS, with residual risk
Martin–Odlyzko–Wolfram (1984) and Lettieri–Stevens–Thomas (2006) provide general additive-automaton algebra and periodicity methods, not the inspected closed twisted-seam comparison. The closest prior untwisted prism calculation does not imply the Möbius root multiplicity; a Möbius majority model uses a different nonlinear update. The arXiv Cayley-tree boundary result treats a different graph family. Full bodies of Dow (1997) and Ganguly–Sikdar–Chaudhuri (2008) were inaccessible; an unindexed equivalent or a stronger specialization of general methods is a live historical risk. Details of aliases, stronger coverage, databases and implication comparisons appear in `AUDIT.json`.

## Mathematical value — PASS
The prism/Möbius pair is a natural controlled change of spatial boundary identification. A local seam twist keeps recurrent-state counts and eventual-phase fibre cardinalities unchanged while changing sharp entry times and the entire transient histogram. The exact modulo-three and two-adic trichotomy quantifies a boundary effect not detectable by the attractor census alone.

## Limits
The claim applies only to binary synchronous open-neighbour XOR on the two defined cubic graph families, not to other update rules or general cubic graphs. The Möbius period counts are given by exact polynomial-gcd formulas; independent literature and mathematical audit are not claimed.

Self-review: passed. Independent audit: not yet performed.
