# One-cell rank-3 Mercat verification at genus 11: no semistable (3,20,7)

## Context

Rank-2 Mercat bounds are settled for general curves (Farkas-Ortega for genus
11; Bakker-Farkas for generic curves of every genus). The live frontier is
rank 3 on general curves, where no all-genus theorem exists. The cell
$(n,d,k)=(3,20,7)$ at $g=11$ is Brill-Noether negative and a strict
Mercat-type violation, hence the field-standard one-cell progress unit.

## Definitions

- $C$: smooth projective curve of genus $g=11$; "general" means outside a
  finite union of proper closed Brill-Noether loci in $M_{11}$.
- For a bundle $E$ of rank $n$, $\gamma(E)=(d_E-2(h^0(E)-n))/n$.
- Classical Clifford index of a general genus-$11$ curve: $\mathrm{Cliff}_1=5$.
- Brill-Noether number of the cell:
  $\rho=n^2(g-1)+1-k(k-d+n(g-1))$; here
  $\rho=90+1-7(7-20+30)=-28$.
- Gonality values $d_r=\min\{d:\exists\ \text{line bundle},\ h^0\ge r+1\}$;
  on general $g=11$: $d_1=7$, $d_2=10$, $d_4=13$, $d_6=16$, $d_{12}=23$.
- Paranjape-Ramanan lemma: a rank-$n$ bundle with $h^0\ge n+s$ ($s\ge1$)
  and no proper subbundle $N$ with $h^0(N)>\mathrm{rk}\,N$ satisfies
  $h^0(\det)\ge ns+1$, hence $\deg\ge d_{ns}$.

## Result

**Theorem.** Let $C$ be a general smooth projective curve of genus $11$.
Then every semistable rank-$3$ vector bundle $E$ of degree $20$ satisfies
$h^0(C,E)\le 6$. Equivalently, no coherent system $(E,V)$ of type
$(3,20,7)$ with $E$ semistable exists. A bundle with $h^0\ge 7$ would have
$\gamma(E)=(20-2(7-3))/3=4<5=\mathrm{Cliff}_1(C)$, so the rank-3
Mercat-type bound $\gamma\ge 5$ holds in this cell.

**Corollary (Butler generated-case exclusion).** A fortiori there is no
generated $\alpha$-semistable $(E,V)$ of type $(3,20,7)$ with $E$
semistable on a general (hence Cliff-$5$) genus-$11$ curve. The Butler
kernel of a putative generated system would have rank $4$, degree $-20$,
slope $-5$.

## Proof / evidence

Priors used (not re-proved): classical line-bundle Brill-Noether bounds on
a general genus-$11$ curve and the Paranjape-Ramanan lemma. No rank-2
Mercat theorem is a logical input.

1. Assume semistable rank-$3$ $E$, $\deg E=20$, $h^0(E)\ge 7=3+4$.
   Paranjape-Ramanan with $n=3,s=4$ gives: absent a witness subbundle with
   $h^0>\mathrm{rk}$, $h^0(\det E)\ge 13$; but $\det E$ has degree $20$
   while $h^0\ge 13$ needs $d\ge 23$ (Riemann-Roch sharpens to $\le 11$).
   Hence some saturated proper $N\subset E$ (rank $1$ or $2$) has
   $h^0(N)>\mathrm{rk}\,N$.
2. A line witness $L$ with $h^0\ge 2$ has $\deg\ge 7$ but semistability
   caps line subbundles at $\lfloor 20/3\rfloor=6$: impossible. A rank-$2$
   witness $N$ with $h^0\ge 3$ either has no $h^0\ge 2$ line (then
   Paranjape-Ramanan $n=2,s=1$ gives $\deg N\ge d_2=10$) or contains one
   (degree $\ge 7$, saturating in $E$ to degree $\ge 7>6$, impossible).
   Hence $10\le\deg N\le\lfloor 40/3\rfloor=13$.
3. $N$ cannot be unstable: with $0\to M_1\to N\to M_2\to 0$,
   $m_1>m_2$, $m_1\le 6$, a degree $\le 6$ line has $h^0\le 1$, so
   $h^0(M_1)+h^0(M_2)\le 2<3$ exhaustively. Thus $N$ is semistable.
4. On semistable $N$: if no $h^0\ge 2$ line, $h^0(N)\ge 4$ forces
   $h^0(\det N)\ge 5$, i.e. $\deg N\ge d_4=13$; $h^0(N)\ge 5$ forces
   $\ge 7$ sections of $\det N$, i.e. $\deg N\ge d_6=16$. The alternative
   (an $h^0\ge 2$ line) already contradicts semistability of $E$.
   So $h^0(N)\le 3$ for $d_N\le 12$ and $\le 4$ for $d_N=13$.
5. From $0\to N\to E\to Q\to 0$ ($\mathrm{rk}\,Q=1$, $d_Q=20-d_N$),
   $h^0(E)\le h^0(N)+h^0(Q)$: $(d_N,d_Q)=(10,10)\to 3+3=6$;
   $(11,9)\to 3+2=5$; $(12,8)\to 3+2=5$; $(13,7)\to 4+2=6$.
   In all cases $h^0(E)\le 6$, contradicting $h^0\ge 7$. ∎

## Limitations

- Logical inputs are classical line-bundle Brill-Noether bounds plus the
  textbook Paranjape-Ramanan lemma; the argument is deductive, and
  `verify_target.py` replays only the arithmetic.
- "General" is non-effective (finite union of BN loci in $M_{11}$).
- Decides only the $(3,20,7)$ ($\gamma=4$) violation sub-cell, not the
  $(20,6)$ sub-case nor all-genus rank-$3$ Mercat.
- K3-section rank-$3$ violations (Farkas-Ortega, Feyzbakhsh) are the
  opposite direction and untouched.

## Reproducibility

Run `python3 output/artifacts/verify_target.py` (stdlib only); expect
`VERIFY_OK`. It replays $\mu=20/3$, $\gamma=4$, $\rho=-28$, the BN
thresholds, semistability caps, the Rank-2 Paranjape-Ramanan caps, the
Riemann-Roch cap, the unstable-pair exhaustion, and the four
$(d_N,d_Q)$ totals.

## References

- Farkas, Ortega, Higher rank Brill-Noether theory on sections of K3
  surfaces, arXiv:1102.0276.
- Bakker, Farkas, The Mercat Conjecture for stable rank 2 vector bundles
  on generic curves, arXiv:1511.03253.
- Lange, Newstead, Bundles of rank 3 on curves of Clifford index 3,
  arXiv:1211.6710 (Paranjape-Ramanan Lemma 2.2; Cliff-3 scope boundary).
- Feyzbakhsh, An effective restriction theorem via wall-crossing and
  Mercat's conjecture, arXiv:1608.07825.
- Bajravani, Ortega, Linear stability and rank two Clifford indices,
  arXiv:2509.06149.
- Hitching, Hoff, Newstead, Nonemptiness and smoothness of twisted
  Brill-Noether loci, arXiv:1804.01260.
