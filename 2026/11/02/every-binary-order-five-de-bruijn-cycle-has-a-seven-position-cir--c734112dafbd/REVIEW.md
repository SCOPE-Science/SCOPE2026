# Independent mathematical audit

## correctness

PASS

All 32 length-five factors occur once, so at least ceil(32/5)=7 marks. Any seven marks hitting all length-five windows have positive gaps <=5 with deficits summing to three; 84 ordered deficit vectors yield exactly 384 distinct indexed candidate sets. Such a candidate hits all longer factors by the uniquely occurring length-five prefix; 30 short factor masks decide remaining lengths one through four. Exhaustively enumerate 2^16 shift-compatible state successor choices, the 2048 cycles with a single 32-cycle, and all 384 candidates. An independent Euler-tour enumeration supplies a second proof of completeness.

## originality

PASS

Best-of-knowledge original in its precise qualified statement. Prior sources study linearized de Bruijn strings and asymptotic bounds, or an attractor for one Lyndon-generated prime-order construction; the circular cyclic-all-2048, exact indexed multiplicity spectrum and extreme counts are not corollaries of these statements. Circular factor interpretation is essential. Priority limits are recorded; an inaccessible plausible source alone is not treated as automatic failure.

## value

PASS

Circular attractors of de Bruijn cycles are natural minimal factor-hitting sets. This exhaustive order-five phase gives the precise optimum for every cycle and complete extremal distribution, useful as finite benchmark for general all-order questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
