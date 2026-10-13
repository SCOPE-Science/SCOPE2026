# Scientific review: second linear phase for arithmetic triples

## Correctness — PASS
The proof recovers all representation triples by the exact bijection \((x,y,z)\leftrightarrow(s,t,z)\) with \(s=y+2z\) and \(t=x+y+z\). It proves that the claimed maximal gap has exactly \(p\) representations and that the next complete length-\(a\) window has at least \(p+1\) each; monotonicity under addition of \(a\) then covers every larger integer. In particular, the correction \(\delta\) for the saturated second lattice band is controlled by a third band through \(d\le h\). Both endpoints \(p=h+1\) and \(p=a+d\), the smallest \(a=3\), and the integer coprimality condition are accounted for. Exact finite cross-checks cover \(30{,}750\) parameter triples and \(1{,}940{,}622\) successors, but are not substituted for proof.

## Originality — PASS relative to checked literature
Komatsu–Ying's arXiv:2206.13052, especially introduction, Theorem 1 and its proofs, establishes the three-generator formula only for \(0\le p\le\lfloor a/2\rfloor\), whereas this theorem establishes a new range \(h+1\le p\le a+d\) for odd \(a\) and restricted \(d\). Their formula has slope \(a+2d\); the new range has slope \(a\), so this is not an extension by substitution. Related later works concern Pell triples or longer consecutive-odd generator blocks and do not imply the fixed-triple phase. Neither the checked literature nor the searchable comparison records showed an equivalent. Equivalence in uncatalogued literature remains possible.

## Value — PASS
The literature identifies the transition beyond \(p=\lfloor a/2\rfloor\) as a difficult gap. The finding resolves an entire additional interval of representation thresholds, not an isolated numerical case, and quantifies the change in slope. The proof's three-band saturation correction explains the regime and why the restriction on \(d\) is needed; the boundary instance \((a,d,p)=(5,3,8)\) already fails outside it. The finding does not determine the entire Apéry set or all thresholds.

Self-review: passed. Independent audit: not yet performed.
