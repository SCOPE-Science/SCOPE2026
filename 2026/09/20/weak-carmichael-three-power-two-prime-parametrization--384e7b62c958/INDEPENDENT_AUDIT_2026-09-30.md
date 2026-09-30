# Independent audit — 2026-09-30

**Record:** `2026/09/20/weak-carmichael-three-power-two-prime-parametrization--384e7b62c958`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree:** `9b38b141638cebaa9de2749d238d804130c40a07`  
**Disposition:** passed

## Correctness — PASS

PASS. Starting from the weak-Carmichael Korselt criterion, reduction modulo p-1 and q-1 gives p-1 | Aq-1 and q-1 | Ap-1. With d=p-1 and k=(Ap-1)/(q-1), the bound 1<=k<A follows from q>p, and the identity k(Aq-1)=A^2d+(A-1)(A+k) gives exactly the two divisor conditions after using q-integrality. The converse reverses without an omitted coprimality hypothesis. The prime bounds and p,q congruent to 2 mod 3 follow directly. I independently enumerated all divisor candidates for A=9 from the theorem conditions and reproduced exactly the twelve displayed structural candidates, with only (29,53) and (89,401) prime. The fixed-(p,q) exponent progression is also correct because any one solution makes 3 invertible modulo both p-1 and q-1 and the two congruences intersect in one residue class modulo the lcm of the orders.

## Originality — PASS

PASS. Meštrović's 2013 open preprint explicitly lists 13833=9*29*53 and 321201=9*89*401 in Remark 2.77 and, in the same remark, displays an inconsistent empty-intersection computation for the 9pq slice. The filed divisor theorem supplies a cutoff-free resolution. The complete open-access Wong 1997 thesis was inspected in its pseudo-Carmichael/normal-family section: it gives broad constructions and a converse normal-family condition, but not this finite 3^a p q divisor parametrization, global 9pq classification, or the exact single-residue-class exponent statement. Thus the main previously documented residual risk from Wong's older terminology was materially reduced. No equivalent theorem was located in the 2013/2026 weak-Carmichael sources or tables.

## Scientific value — PASS

PASS. The result converts an infinite search for each fixed a into a finite divisor computation with explicit polynomial-in-A bounds, globally settles a concrete 9pq classification where the prior source is internally inconsistent, and adds an exact periodic lifting statement across exponents. The methods are elementary but structurally useful.

## Findings

- Independent exact-integer enumeration at A=9 reproduces all twelve structural candidates and the two prime solutions.
- Meštrović's 2013 Remark 2.77 both lists the two 9pq examples and contains an incompatible empty-search statement.
- The full Wong thesis section on pseudo-Carmichael normal families does not state the audited special parametrization or classification.

## Independent checks

- Re-derived the d,k parametrization and its converse from the weak-Carmichael divisibility criterion.
- Recomputed the A=9 divisor table independently using exact integer arithmetic.
- Checked the multiplicative-order argument and the required invertibilities in the exponent-period corollary.
- Inspected older pseudo-Carmichael terminology in Wong's full thesis, not merely indexed metadata.

## Literature evidence

- https://doi.org/10.1090/crmp/011/02 — Borwein and Wong (1997), Giuga-type congruence context for the divisibility characterization.
- https://arxiv.org/abs/1305.1867 — Meštrović (2013), weak Carmichael criterion and Remark 2.77 containing both 9pq examples and the inconsistent computation.
- https://www.collectionscanada.gc.ca/obj/s4/f2/dsk2/ftp04/mq24272.pdf — E. Wong (1997), full M.Sc. thesis using the older pseudo-Carmichael/normal-family terminology; inspected for possible covering specializations.
- https://oeis.org/A225498 — Weak Carmichael number table context; does not supply the filed fixed-a divisor classification.

## Limitations

- The theorem treats 3^a p q with p and q distinct and occurring to the first power only.
- Four-or-more-prime support and larger p- or q-exponents are not classified.
- Originality is still literature-limited even after inspection of the principal older pseudo-Carmichael source.

No GitHub write was performed by this audit. The guarded change set only stages this audit evidence and updates the independent-audit channel in `VERIFICATION.md`; it leaves the research claim files unchanged.
