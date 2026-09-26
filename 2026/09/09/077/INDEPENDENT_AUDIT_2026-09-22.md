# Independent audit — 2026/09/09/077

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

For J_t, each signed support-S vertex is ±1_S/(1+t|S|); the polar inequalities on the positive orthant reduce to Σ(y_i−t)_+≤1. This yields the claimed polar polynomial by partitioning according to coordinates above t. I independently evaluated the record's primal inclusion–exclusion formula and polar polynomial with exact rational arithmetic: R(0)=1; R(1/1000)=215378277437/213253198587, R(1/100)=24434731/22283226, R(1/10)=15403/9009, and R(1/4)=4043/1890. Differentiation at zero gives A′(0)=−15, B′(0)=25, hence R′(0+)=10. Each displayed positive t violates 1+4t²; the nonzero linear derivative also rules out any fixed pure quadratic upper envelope near zero. There are Σ_{m=1}^5 binom(5,m)2^m=242 signed support vertices, so J_t for t>0 is not a five-cube. The full Hanner vertex census was not separately exhaustively regenerated.

## Originality — PASS

Kim–Zvavitch, arXiv:1302.5719, give a dimension-dependent qualitative/linear stability theorem, without this particular exact curve's product. The rational volume formulas, slope, and falsification of the proposed C=4 envelope constitute a distinct, limited directional computation.

## Scientific value — PASS

The explicit transverse law and counterexample to a proposed fallback bound clarify local behavior at a cube in dimension five. The uniform κ≥1/16 target and a quantitative distance from every Hanner body remain unproved; the record says so.

Sources: https://arxiv.org/pdf/1302.5719 . Open preprint sufficed.
