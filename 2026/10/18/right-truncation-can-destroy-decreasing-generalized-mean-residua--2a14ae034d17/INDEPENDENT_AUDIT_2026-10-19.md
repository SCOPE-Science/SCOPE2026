# Independent mathematical audit

## correctness

PASS

Original survival is exp(-x) below 1 and exp(-1-(x-1)/3) above; direct integration gives m_X=1+2exp(x-1) below 1 and m_X=3 above. Derivatives of m_X/x are strictly negative and match continuously at the switch. After conditional right truncation at T=1+3log(5/4), S_X(T)=(4/5)e^-1, h_Y(1-)=5, m_Y(1)=3-12log(5/4). Differentiating m/x using m'=h m-1 yields left derivative 11-48 log(5/4). Alternating logarithm Taylor bound log(5/4)<43/192 proves >1/4, on a nontrivial left neighborhood. Independent arbitrary-precision evaluation gives approximately 0.2891095369; exact analytic inequality is decisive. Truncation is X | X<=T, not censoring.

## originality

PASS

The full motivating preprint and later full open-access article explicitly leave DGMRD/DGMRL preservation under right truncation open, while Banciu–Mirchandani proved it for the strictly smaller IGFR class. Exact explicit counterexample answers a natural open binary question; no equivalent published counterexample identified by Resultary and terminology searches, subject to priority limitations.

## value

PASS

An explicit counterexample resolves a question explicitly left open in two papers about lifetime/demand aging classes and identifies that DGMRL is not robust to a standard survival-data operation. The exact elementary law and rigorous margin >1/4 give a reusable witness rather than routine numerical failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
