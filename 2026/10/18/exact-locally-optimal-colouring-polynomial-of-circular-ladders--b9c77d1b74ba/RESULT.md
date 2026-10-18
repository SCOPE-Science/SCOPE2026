# Exact locally-optimal colouring polynomial of circular ladders

## Finding

Let \(P_n=C_n\square K_2\) be the prism graph with two cyclic layers and \(n\ge3\) rungs. For an integer \(k\ge1\), a locally-optimal \(k\)-colouring is any map from its vertices to a named palette \([k]\) for which the vertex's own colour is the **unique plurality** in its open neighbourhood. Write \(L_n(k)\) for the number of such maps; the strict-gridlock count is \(L_n(k)-k\).

**Complete structural classification.** A colouring is locally optimal if and only if it is of precisely one of the following two kinds:

1. Both vertices on rung \(i\) have one colour \(c_i\), for every \(i\), and each letter of the cyclic word \((c_0,\ldots,c_{n-1})\) agrees with at least one cyclic neighbour. Equivalently, each nonconstant monochromatic cyclic run has length at least two.
2. The entire upper cycle has colour \(a\), the entire lower cycle has a different colour \(b\). There are exactly \(k(k-1)\) named assignments of this kind.

Consequently, with \(r\) the number of cyclic monochromatic runs, the full polynomial is

\[
L_n(k)=k^2+\sum_{r=2}^{\lfloor n/2\rfloor}
\frac nr\binom{n-r-1}{r-1}
\bigl((k-1)^r+(-1)^r(k-1)\bigr).
\]

A notably shorter expression uses the integral Lucas-type polynomials
\[
T_0(k)=2,\qquad T_1(k)=1,\qquad
T_n(k)=T_{n-1}(k)+(k-1)T_{n-2}(k),
\]
and the six-periodic integers \(s_n=2\cos(n\pi/3)\), whose successive values starting at \(n=0\) are \(2,1,-1,-2,-1,1\). For every \(n\ge3\),
\[
\boxed{L_n(k)=T_n(k)+(k-1)s_n+k(k-1).}
\]
Equivalently, putting \(\lambda_{\pm}=(1\pm\sqrt{4k-3})/2\),
\[
L_n(k)=\lambda_+^n+\lambda_-^n+2(k-1)\cos(n\pi/3)+k(k-1).
\]
The ordinary generating function, as a formal power series in \(z\), is rational:
\[
\boxed{
\sum_{n\ge3}L_n(k)z^n=
\frac{k^2z^3}{1-z}+
\frac{k(k-1)z^4(2-z)}{(1-z)(1-z-(k-1)z^2)(1-z+z^2)}.
}
\]

The largest number of distinct colours in a locally-optimal colouring of \(P_n\), allowing an arbitrarily large named palette, is exactly \(\max\{2,\lfloor n/2\rfloor\}\). For fixed integer \(k\ge2\), the exact spectral formula additionally gives \(L_n(k)\sim\lambda_+^n\) as \(n\to\infty\). The leading coefficient of \(L_n(k)\), as a polynomial in \(k\), is \(1,3,6\) for \(n=3,4,5\), respectively; for \(n\ge6\) it is \(2\) when \(n\) is even and \(n\) when \(n\) is odd.

## Assumptions and scope

All graphs here are finite simple graphs. The cycle \(C_n\) uses \(n\ge3\), so each prism vertex has three **distinct** neighbours: its two horizontal neighbours and its opposite-rung partner. The palette is named and vertices are labelled; permutations of colours are counted separately. Unused palette colours are permitted. Unique plurality means **strictly more occurrences than any other neighbour colour**. At degree three this is equivalent to at least two neighbours having the vertex's colour. We do not claim this identity for other degrees or for tie-tolerant majority rules. The polynomial can subsequently be evaluated algebraically at arbitrary \(k\), but the colouring interpretation uses integer \(k\ge1\).

## Proof

**Step 1: Classification.** Let \(t_i,b_i\) denote the two colours on rung \(i\), indices taken modulo \(n\). If \(t_i\ne b_i\), the vertical neighbour disagrees with each of these vertices. Each vertex therefore needs **both** horizontal neighbours to have its own colour: \(t_{i-1}=t_i=t_{i+1}\) and \(b_{i-1}=b_i=b_{i+1}\). In particular both adjacent rungs are unequal in exactly the same ordered way. Propagation around the entire cycle forces \(t_j=t_i\) and \(b_j=b_i\) for all \(j\), producing type 2. Conversely every such two-layer colouring is admissible.

If there is no unequal rung, write \(t_i=b_i=c_i\). Each vertex automatically has one agreeing vertical neighbour. It has a strict plurality precisely when at least one of its two horizontal neighbours also agrees. The resulting cyclic words are exactly those in type 1. The two types are disjoint and exhaustive.

**Step 2: Counting type 1.** Constant words contribute \(k\). Every nonconstant admissible cyclic word has \(r\ge2\) maximal monochromatic runs, all of size at least two, so \(2r\le n\). Mark one of its \(r\) boundary edges and choose that boundary among the \(n\) cyclic edges. Starting after that boundary, the \(r\) run lengths form a composition of \(n\) into positive integers at least two, of which there are \(\binom{n-r-1}{r-1}\). Each unmarked boundary set is counted exactly \(r\) times, so the number of boundary sets is \(\tfrac nr\binom{n-r-1}{r-1}\). Assigning colours to these ordered cyclic runs with neighbouring runs distinct has the usual cycle chromatic-polynomial value \((k-1)^r+(-1)^r(k-1)\). For \(r=2\), the two cyclic adjacencies simply both demand distinct colours, and the same expression is \(k(k-1)\). Adding the type-2 contribution \(k(k-1)\) to the constant-word contribution \(k\) gives the displayed finite sum.

**Step 3: Lucas and periodic form.** Set \(w(z)=z^2/(1-z)\), the generating series for run lengths at least two. The nonconstant type-1 contribution to the generating function is the coefficientwise derivative \(z\tfrac{d}{dz}H(z)\), where
\[
H(z)=\sum_{r\ge2}\frac{(k-1)^r+(-1)^r(k-1)}r\,w(z)^r.
\]
All identities are formal, so no analytic convergence is required. Summing the logarithmic series and simplifying yields
\[
H(z)=k\log(1-z)-\log(1-z-(k-1)z^2)-(k-1)\log(1-z+z^2).
\]
Factor \(1-z-(k-1)z^2=(1-\lambda_+z)(1-\lambda_-z)\), where \(\lambda_++\lambda_-=1\) and \(\lambda_+\lambda_-=1-k\). Also \(1-z+z^2=(1-e^{i\pi/3}z)(1-e^{-i\pi/3}z)\). The coefficient of \(z^n\) in \(zH'(z)\) for \(n\ge1\) is
\[
\lambda_+^n+\lambda_-^n+2(k-1)\cos(n\pi/3)-k.
\]
Add \(k\) for the constant-rung type-1 words and \(k(k-1)\) for type 2. This proves the spectral expression. The sequence \(\lambda_+^n+\lambda_-^n\) satisfies the stated integer recurrence with initial values \(2,1\), which proves the Lucas form without dependence on complex-number branches.

Taking the formal derivative of the logarithms, or directly summing the finite formula, yields the rational generating function. In particular, the nonconstant-run generating function simplifies to
\[
\frac{k(k-1)z^4(2-z)}{(1-z)(1-z-(k-1)z^2)(1-z+z^2)}.
\]
The \(k^2z^3/(1-z)\) summand accounts for the consensus words and the two-layer unequal assignments at every permitted \(n\ge3\).

**Step 4: Degree, leading coefficient and growth.** A type-2 colouring uses two distinct colours; a type-1 colouring with \(r\ge2\) runs uses at most \(r\le\lfloor n/2\rfloor\) colours. Each maximum is attained: use two different monochromatic layers, or run lengths of two (and one length three when \(n\) is odd) with distinct run colours. This gives the maximum. For \(n\ge6\), maximal run structures have \(2\) boundary sets for even \(n\), or \(n\) for odd \(n\), each contributing a monic degree-\(\lfloor n/2\rfloor\) cycle chromatic polynomial; the vertical case contributes degree two only. For \(n=3,4,5\), direct substitution in the finite formula gives \(k^2\), \(3k^2-2k\), \(6k^2-5k\). Finally, for integer \(k\ge2\), the root \(\lambda_+>1\) strictly dominates \(|\lambda_-|\); the six-periodic and constant terms are bounded, proving the stated asymptotic.

## Verification

Run `python verify_prism.py` using Python 3 and only the standard library. The program independently tests the original **vertex-neighbour plurality rule** by exhaustive assignment enumeration, then separately tests the classification and finite formula. It checks \(14\) parameter pairs: \(k=2\), \(3\le n\le9\); \(k=3\), \(3\le n\le6\); and \(k=4\), \(3\le n\le5\), a total of \(2{,}065{,}492\) labelled assignments. All passed. Independently, it checks the Lucas formula at \(147\) integer points and the rational generating series for nine palette evaluations through degree \(30\); all passed. These finite computations check implementation and boundary cases but are not the proof of the result for unrestricted \(n,k\).

## Relationship to prior work

Jones and Winkeler, *Counting Strict Gridlock on Graphs* (arXiv:2603.18289v1, first posted 18 March 2026), introduce locally-optimal and strict-gridlock colourings and give a general recurrence for subcubic graphs. Their stated recurrence permits algorithmic counting on a prism, but the work does not state the prism structural dichotomy, run-count coefficient formula, Lucas-plus-periodic identity, or rational family generating function. The definition and that general recurrence are fully credited; the claim here is the explicit infinite-family evaluation, not the invention of the colouring rule or its generic computability.

Shukla, *Voter dynamics on an Ising ladder: coarsening and persistence* (2005), discusses binary frozen domains with minimum length two under zero-temperature Ising/Glauber dynamics on a ladder. This anticipates one of the structural mechanisms in the two-colour specialization; that earlier binary observation is not claimed as new. It does not state the all-palette locally-optimal polynomial or its six-periodic spectral correction. The exact number of unrestricted named-palette fixed points is distinct from the dynamical questions studied there.

## Limitations

The theorem concerns labelled named-palette maps on cubic circular ladders only. It is not a characterization of fixed points on arbitrary graphs, not an evaluation of probability of reaching a state under stochastic updates, and not a counting formula for different synchronous tie-breaking conventions. The previous literature already establishes a generic counting algorithm and binary-domain phenomena; these are not new contributions. Bibliographic searches and primary-paper comparison cannot establish absolute priority in unindexed or differently named literatures. No independent validation has been performed.

## References

1. Matthew I. Jones and Zachary Winkeler, *Counting Strict Gridlock on Graphs*, arXiv:2603.18289v1 (18 March 2026), https://arxiv.org/html/2603.18289 .
2. Prabodh Shukla, *Voter dynamics on an Ising ladder: coarsening and persistence*, Journal of Physics A: Mathematical and General 38 (2005), 5441–5451, doi:10.1088/0305-4470/38/24/004 .
