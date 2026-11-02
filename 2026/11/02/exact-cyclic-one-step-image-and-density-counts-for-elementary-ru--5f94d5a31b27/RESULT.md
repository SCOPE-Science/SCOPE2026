# Exact cyclic one-step image and density counts for elementary Rule 18

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous elementary cellular automaton Rule 18, on indexed cyclic cells with all indices interpreted modulo \(n\ge1\):
\[
 F_n(x)_i=(1-x_i)(x_{i-1}\oplus x_{i+1}).
\]
For a nonzero binary output \(y\), list its \(m\) one-positions \(p_0<\cdots<p_{m-1}\) in cyclic order, and set \(g_j\) to the number of zeros from \(p_j\) to \(p_{j+1}\) clockwise, with indices modulo \(m\). Then \(y\) has a predecessor of the **same period length** \(n\) if and only if \(m=2k\) is even and at least one of the two alternating gap classes is strictly positive:
\[
 (g_0,g_2,\ldots,g_{2k-2}>0)\quad\text{or}\quad
 (g_1,g_3,\ldots,g_{2k-1}>0).
\]
The all-zero output is reachable for every \(n\). Whenever the condition holds, a predecessor is obtained explicitly by pairing the one-positions along the cyclic direction so that each interval *between* pairs contains at least one zero, putting input zeros throughout each paired arc and input ones throughout the interpair arcs.

Let \(R_{n,2k}\) count indexed cyclic outputs of length \(n\) with exactly \(2k\) ones that possess an \(n\)-periodic predecessor. For all positive integers \(n,k\),
\[
 R_{n,2k}=\frac{n}{2k}\left[2\binom{n-k-1}{2k-1}-\binom{n-2k-1}{2k-1}\right],
\]
where \(\binom{a}{b}=0\) whenever \(a<0\), \(b<0\), or \(b>a\). Every odd positive output weight has count zero, and \(R_{n,0}=1\). Defining \(a_n=\sum_kR_{n,2k}\), the all-length generating function is
\[
 \sum_{n\ge1}a_nz^n
 =-z\frac{Q_1'(z)}{Q_1(z)}+\frac z2\frac{Q_2'(z)}{Q_2(z)},
 \quad Q_1(z)=1-2z+z^2-z^3,\quad Q_2(z)=1-2z+z^2-z^4.
\]
In particular, with \(\lambda\approx1.75487766624669\) the real root greater than one of \(t^3-2t^2+t-1=0\), and \(\varphi=(1+\sqrt5)/2\),
\[
 a_n=\lambda^n-\tfrac12\varphi^n+O(1).
\]
The image occupies an asymptotic fraction \((\lambda/2)^n(1+o(1))\) of all indexed binary ring states.

## Assumptions and scope

Words are binary and **indexed**: rotations are different configurations if their bits at indexed positions differ. Input and output have identical ring length, including the small rings \(n=1,2\); no predecessor with a longer spatial period is allowed. All image statements refer to exactly **one** synchronous update. The zero-gap vector is cyclic: the final gap from the last one to the first is included. The alternating-gap condition is existential in the two choices of pairing and is independent of the initial cyclic one-position chosen. Binomial coefficients use the zero convention stated above.

## Proof

**Local pairing lemma.** If the input contains no ones, the output is zero. Otherwise partition its cyclic zeros into maximal runs separated by input ones. Input one-cells always output zero. A zero-run of length one outputs zero, because its zero-cell has two one-neighbors. For a zero-run of length at least two, its first and last cells output one (each has one neighboring input one and one neighboring input zero); every interior cell outputs zero. Thus all output ones occur as two endpoints of zero-runs of length at least two. The two endpoints form a pair. Consecutive pairs are separated by at least one output zero, at the intervening input one-cell(s). This forces even output weight and one of the two alternating classes of consecutive-one gaps to be positive. The argument remains valid for a single input one and all small rings.

**Sufficiency and explicit inverse.** For a nonzero output satisfying the stated gap condition, choose the corresponding pairing of consecutive output one-positions. On every clockwise arc from the first to the second endpoint of a pair, assign all input cells zero. On every complementary interpair arc, assign all input cells one. Each pair arc has at least two zero-cells; each interpair arc has at least one one-cell. The local pairing lemma applied to this constructed input gives one precisely at the two endpoints of every pair arc and zero everywhere else. The constructed input therefore maps exactly to the given output. The all-zero output is obtained from the all-zero input. This proves necessity and sufficiency without any finite-size assumption.

**Fixed-weight count.** Fix \(n\) and positive \(k\) and distinguish a one-position in an indexed output with \(2k\) ones. Choosing the distinguished index in \(n\) ways determines a unique ordered vector of \(2k\) nonnegative gaps summing to \(n-2k\). By stars and bars, the number of such vectors for which the odd-indexed \(k\) gaps are each at least one equals \(\binom{n-k-1}{2k-1}\), and the same number occurs for the even-indexed gaps. Their intersection, in which every gap is positive, has \(\binom{n-2k-1}{2k-1}\) vectors. Inclusion–exclusion, followed by division by \(2k\) choices of distinguished output one-position, yields exactly the formula for \(R_{n,2k}\). This counts indexed words, not necklaces, even for periodic outputs.

**Generating function.** Set \(B(z)=z^3/(1-z)^2\) and \(C(z)=z^2/(1-z)\). A marked clockwise pair of output ones with a possibly empty internal zero gap and a nonempty following interpair zero gap contributes a block of generating function \(B\). There are two possible directed alternating pairings, and counting output–pairing incidences gives
\[
 \sum_{k\ge1}\frac nk[z^n]B(z)^k
 =[z^n]\frac{zB'(z)}{1-B(z)}.
\]
An output is counted twice precisely if **all** its consecutive-one gaps are nonempty. These have \(2k\) consecutive blocks \(10^{\ge1}\), each with generating function \(C(z)\), and the one-copy overcount is
\[
 \sum_{k\ge1}\frac n{2k}[z^n]C(z)^{2k}
 =[z^n]\frac{zC(z)C'(z)}{1-C(z)^2}.
\]
There is exactly one zero output of each positive length. Consequently
\[
 \sum_{n\ge1}a_nz^n=
 \frac z{1-z}+\frac{zB'(z)}{1-B(z)}
 -\frac{zC(z)C'(z)}{1-C(z)^2}.
\]
Writing \(1-B=Q_1/(1-z)^2\) and \(1-C^2=Q_2/(1-z)^2\), differentiating logarithms, and cancelling the terms with denominator \(1-z\) gives the stated rational logarithmic derivative.

**Asymptotics.** The reciprocal roots of \(Q_1\) are the three roots of \(t^3-2t^2+t-1\): one real root \(\lambda>1\) and a conjugate pair each of modulus \(\lambda^{-1/2}<1\). The reciprocal roots of \(Q_2=(1-z-z^2)(1-z+z^2)\) are \(\varphi\), \(-\varphi^{-1}\), and the two conjugate sixth roots of unity. Extracting coefficients from the logarithmic derivatives yields \(a_n=\lambda^n-\varphi^n/2+O(1)\), and division by \(2^n\) gives the fraction statement. The implied bound holds uniformly over integer \(n\ge1\).

## Verification

The standalone `verify.py` independently computes all cyclic Rule-18 outputs directly from each input bit tuple, checks the alternating-gap decision against the complete forward image, and constructs and tests an actual predecessor for **every** accepted candidate output. It does this for every \(1\le n\le18\), checking each output weight against the closed binomial formula. A separate integer-arithmetic logarithmic-derivative recurrence tests the total counts against the binomial sum through \(n=70\). Run from this directory with `python verify.py`; success prints `VERIFY_OK`. These exhaustive finite tests support, but do not replace, the all-length proof above. The first eighteen total image counts are
\[
 1,1,4,7,11,19,36,67,121,216,386,691,1236,2206,3929,6987,12411,22024.
\]

## Relationship to prior work

The original Rule-18 transducer and attracting-domain studies of Hanson and Crutchfield give general regular-language techniques and describe long-time attractor structure; they do not establish the present fixed-period one-step image classifier or weight-by-weight counts. Jen developed general preimage recurrences and separately investigated cyclic attractors; a closely related cyclic-attractor paper was accessible only at abstract level, so a historical overlap risk remains. Meunier's earlier computational-complexity classification treats prediction and intrinsic universality, not the density-refined periodic image. Sabrié and Törmä later observe that outputs containing `111`, or `11v11` for a middle factor with an odd number of ones, cannot have preimages; this supplies related **necessary** obstructions but does not provide the cyclic sufficiency, constructive predecessor or exact image enumeration proved here. General finite-state and transfer-matrix techniques can in principle count images, but algorithmic computability alone does not give these expressions. The result is a specialized exact characterization, not a new general decidability theorem.

## Limitations

The theorem addresses one synchronous step only. It does not count the number of distinct predecessors of each reachable word, analyze trajectories after multiple updates, or address stochastic or nonperiodic boundary conditions. The archival literature comparison is based on accessible full texts and available metadata; no independent historical-priority determination is claimed. The inaccessible full text of Jen's cyclic-attractor article is an explicit residual literature risk, although its stated subject is eventual cycles, not one-step image counts.

## References

- J. E. Hanson and J. P. Crutchfield, *The Attractor-Basin Portrait of a Cellular Automaton*, Santa Fe Institute Working Paper 91-02-012 (1991), full working paper: https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/aa/5a/aa5a7d95-aa45-4ca8-a057-c2b154d34d12/91-02-012.pdf .
- E. Jen, *Scaling of Preimages in Cellular Automata*, Complex Systems **1** (1987), 1045–1062, full text: https://content.wolfram.com/sites/13/2018/02/01-6-2.pdf .
- E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics **118** (1988), 569–590, https://doi.org/10.1007/BF01221109 .
- P.-É. Meunier, *Unraveling simplicity in elementary cellular automata*, arXiv:1406.5306v1, publicly submitted 2014-06-20, https://arxiv.org/abs/1406.5306 .
- É. Sabrié and I. A. Törmä, *Limit dynamics of elementary cellular automaton 18*, Ergodic Theory and Dynamical Systems (2026), https://doi.org/10.1017/etds.2026.10300 .
