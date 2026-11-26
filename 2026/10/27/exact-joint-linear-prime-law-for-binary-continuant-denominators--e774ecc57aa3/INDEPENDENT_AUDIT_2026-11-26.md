# Independent mathematical audit

## correctness

PASS

At each root the consecutive pair starts at a=(1,0); the other possible states are b=(0,1), c=(1,1). Evaluation 0 swaps a and b and fixes c; evaluation 1 cycles a to c to b to a. Since the next two evaluations of a letter are complementary and both letters occur among the extensions, one can independently reconstruct the joint transfer on unordered pairs of states: aa and cc each go twice to bc, bb goes twice to aa, ab and bc each go once to ab and once to ac, and ac goes once to bb and once to cc. From aa the first successive count multisets are aa, 2bc, 2ab+2ac, 2ab+2ac+2bb+2cc, and 2ab+2ac+2bb+2cc+4aa+4bc. Thus v_4=v_3+2v_1+4v_0 on this quotient and the fixed linear transfer gives the recurrence for all degrees. Summing aa, ac and cc gives initial J_d of 1,0,2,4 and generating function 4/[9(1-2z)]+4/[9(1+z)]+(1-4z)/[9(1+2z^2)], which reproduces both parity formulas. At one root all extensions from b avoid the root and exactly one extension from either a or c avoids it, giving L_{d+1}=2^{d+1}-L_d and L_0=1. Inclusion-exclusion and J_d/2^d-(L_d/2^d)^2 reproduce the table, the independence limit and both covariance expressions, including zero at d=0 and alternating signs on each parity thereafter. The normalized oscillatory part has sharp magnitude proportional to 2^{-d/2}. Polynomial continued fractions with the prescribed degrees are in bijection with their ordered words by Euclidean division, and denominators are the monic continuants, so orthogonal multiplicity gives the word law, not the uniform monic law. In the uniform monic model d>=2, the independent linear and constant coefficients already give a uniform evaluation pair. The source's state order is the product order induced by the displayed list a,b,c, not numeric lexicographic order on binary tuples; the displayed vectors use the correct order.

## originality

PASS

Credit the exact weighted two-linear-place table and finite-degree covariance. The inspected same-object primary paper supplies the word parametrization, an unweighted support-count formula and local results for nonlinear factors; none of those gives the exact joint linear-place law. The strongest same-alphabet antecedent and closest Resultary residue record have different counted objects or exclude the two places. This is a bounded assessment, not a priority guarantee.

## value

PASS

The two linear factors exhaust the linear places of the binary field and are naturally coupled by the complementary evaluations of the two letters. Their joint law in the multiplicity measure is not the uniform-monic law or an independence assumption: it gives a sharp oscillating dependence correction, including its decay scale and sign, to the asymptotic 4/9 joint avoidance. This is useful exact local information for the natural word/multiplicity ensemble, without claiming to solve the unweighted denominator-count problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
