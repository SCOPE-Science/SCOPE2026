# Independent mathematical audit

## correctness

PASS

Direct Hardy–Weinberg viability selection gives F_s=N_s/D_s, N_s=x[1+s(h+(1-h)x)], D_s=1+s[2hx+(1-2h)x²]>0. A positive fitness-tilted binomial K yields F_s'(x)=Var_w(K)/(2x(1-x))>0. Frozen polynomial commutator for strengths a>b>0 has strictly positive denominator and factor ab(a-b)x²(1-x)²U_h(x)² Q_{h,a,b}(x), with U_h=h+(1-2h)x and Q=(1-h)(1-x)+hx[1+a+b+ab(h(1-x)+x)]. On h in [0,1], U,Q>0, so adjacent exchanges and strict monotonicity of following maps prove unique (mod equal strengths) descending maximum and ascending minimum for any finite horizon and x in (0,1). At h>1 Q(0)<0<Q(1) and Q is a concave quadratic, with one root below common equilibrium x*=h/(2h-1); commutator reverses sign below that root and also vanishes at x*. Independently evaluated exact witness h=2,a=2,b=1: differences at x=1/20 = -7907344/26731501383, x=1/4 = 100/47117, x=2/3=0. Actual symbolic checker code contains complete factorization test; finite spot checks are supporting, not infinite proof.

## originality

PASS

Qualified PASS for exact all-horizon strength permutation extremality and h=1 sharp dominance boundary. Earlier temporally variable genetic selection studies focus on polymorphism persistence, fixation and changing favored allele; none of the inspected statements implies the same-direction fixed-positive-strength commutator sign and optimal sorting. Relevant 1974/1976 Hedrick technical PDF content not fully read; historical priority remains open.

## value

PASS

A nontrivial global rearrangement principle for nonlinear rational allele-frequency maps, with sharp crossover to overdominant behavior. It classifies all finite permutations for a natural one-locus model and provides an exact minimal two-epoch failure regime beyond h=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
