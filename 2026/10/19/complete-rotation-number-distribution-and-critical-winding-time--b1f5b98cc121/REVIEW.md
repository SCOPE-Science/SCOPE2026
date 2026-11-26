# Independent mathematical audit

## correctness

PASS

Frozen correctness fails: the exact off-node piecewise-quadratic CDF and its density rely on the false parenthetical ‘in fact, linearly’ in the paragraph after Ostrovski's Theorem 5.1. The same primary source separately establishes the geometric foliation, with parallel intervening polygon sides and continuity (Corollary 5.4); the repair does not use the linearity assertion. In the leaf qP₁ the K corner edges have area Jacobian qtd apiece because det B=1 and Bv₀=(t,s) give det(v_j,v_{j+1})=−td, and the horizontal side segment of length 1−q contributes t(1−q) per unit dq. Hence the area disintegration gives total leaf mass M(q)=4t[1−(1−Kd)q], so the outside area is 4tq−2t(1−Kd)q², strictly increasing on 0≤q≤1. The map preserves q and area, so it preserves the atomless full-support conditional circle measure for a.e. q. The orientation-preserving action in the normalized cumulative-mass coordinate is a rotation, with displacement qtd/M(q) measured on the arc qv₀→qv₁. Continuity gives this ratio on every interior leaf. Thus q(r)=4r/[d+4(1−Kd)r], not affine interpolation. At K=3, r=1/14, the exact q is (1+d/2)⁻¹ and the frozen q is (1+3d/7)/(1+d); their exact positive difference is (30√2−41)/833. Since outside area increases strictly, this refutes the frozen CDF. The corrected rational law and density are obtained by substitution and differentiation; endpoints give no atoms, r(q_N)=1/[4(K+N)], and the original node laws, leading tail, and logarithmic truncated mean survive. The repaired moment statement quantifies all real exponents p<1 since T≥4K also bounds negative moments. I independently reduced the determinant, first-step and left-eigenvector identities modulo s²=t(1−t), f²=1−4t² and expanded the two logarithms in √(1/2−t); their coefficients match the repaired derivation of 4K²−32K/3+128/45. The frozen finite script was inspected, not executed; its integer-index polygon tests could not detect the off-node error. Complete corrected result, verification notes (original front matter preserved), and slogan are provided separately; the frozen package is unchanged. This PASS is for those corrected scientific claims, not for the original interpolation.

## originality

PASS

On the repaired claim, the distinct parts are the correct off-node rotation coordinate and full area pushforward, which correct the interpolation assertion in the motivating paper, and the displayed higher-order large-K asymptotic of the leading coefficient. The foliation, distinguished levels and earlier core area are prior inputs. The exact node-law and leading tail overlap substantively with a separately indexed but later-dated finding; they are not counted as the distinguishing content here.

## value

PASS

The corrected formula gives a canonical area distribution at all rotation thresholds on a natural positive-area invariant annulus, rather than just at selected periodic boundaries. It resolves a concrete error in the original off-node rotation description, yields the exact reciprocal survival law with its finite-moment cutoff, and separates the leading rare-slow-rotation coefficient from the tail's higher-order resonant scaling. This is a useful exact invariant and correction of prior literature, not a routine recomputation of one core area.

The dated certificate retains the supplied scientific assessment, sources and limitations.
