# Sharp second-largest cyclic preimage fibers of elementary cellular automaton Rule 18

## Finding
For every integer \(n\ge7\), let \(f_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous elementary cellular automaton Rule 18 with cyclic indexing, and write \(d_n(y)=|f_n^{-1}(y)|\). Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). The all-zero output is the unique most probable image of a uniformly random input, and
\[
d_n(0^n)=F_{n-1}+F_{n+1}+1.
\]
Among every other output the exact largest fiber is
\[
\max_{y\ne0^n}d_n(y)=F_{n-2}.
\]
Equality holds precisely for the \(n\) indexed cyclic words with exactly two ones in adjacent positions; no other nonzero output attains it.

More generally, an exact formula computes \(d_n(y)\) at every ring size \(n\ge1\). An output with an odd number of ones has no predecessor. When its \(2r\ge2\) ones occur at cyclic positions \(p_0<p_1<\cdots<p_{2r-1}\), take the two alternating pairings of these positions into \(r\) consecutive pairs in cyclic order. In each pairing, suppose the pairs are \((s_j,e_j)\) for \(j=0,\ldots,r-1\), listed cyclically. Let \(t_j\) be the number of positions strictly between the closing endpoint \(e_j\) and the next opening endpoint \(s_{j+1}\), in the forward cyclic direction. Define the pairing weight as zero if any \(t_j<1\), and otherwise as \(\prod_{j=0}^{r-1}F_{t_j}\). Then \(d_n(y)\) is the sum of the two pairing weights. This formula also applies at \(n=1,2\), with cyclic positions interpreted modulo \(n\).

## Assumptions and scope
The alphabet is binary. Indices lie in \(\mathbb Z/n\mathbb Z\), with an indexed rather than rotation-identified ring. The local update is exactly
\[
(f_n(x))_i=1\quad\Longleftrightarrow\quad(x_{i-1},x_i,x_{i+1})\in\{(0,0,1),(1,0,0)\},
\]
which is Wolfram Rule 18. Every input has equal probability \(2^{-n}\). A fiber counts labeled configurations, not rotation classes. The modal ranking theorem requires \(n\ge7\); the exact pairing formula is valid for every positive \(n\). No assertion is made about multiple time steps or other rules.

## Proof
**1. Structure of preimages.** A nonconstant input containing at least one zero and one one decomposes cyclically into maximal zero runs separated by nonempty runs of ones. A zero run of length at least two produces output ones at precisely its two endpoints. A singleton zero produces no output one, and each input one produces output zero. Consequently every positive output has an even number of ones, and each long zero run pairs two successive output ones. The long zero runs determine one of the two alternating pairings of all output ones.

Fix a pairing of an output with \(2r\) ones. Declare the entire stretch from each opening to its closing endpoint to be a zero run. To keep these runs maximal, the stretches between successive closing and opening endpoints must begin and end in an input one and contain no adjacent zeros. If a stretch has \(t\) sites, its number of fillings is \(F_t\): for \(t=1,2\) there is one filling, and for \(t\ge3\) splitting by the second site yields the usual Fibonacci recurrence. If \(t<1\), this pairing is impossible. The stretches are independent; multiplying their counts and summing the two mutually exclusive pairings proves the general formula. Different pairings give disjoint input sets because a long zero run has uniquely determined endpoints. The all-zero input produces all-zero output, but has no ones-run decomposition and is separately counted below.

**2. The zero-output fiber.** In any mixed input, output zero at every site exactly when there is no cyclically adjacent pair of input zeros. The all-one input is included; the all-zero input is an additional solution. The cyclic no-adjacent-zero binary configurations are counted by the Lucas number \(L_n=F_{n-1}+F_{n+1}\), including the small-ring interpretations \(n=1,2\). Hence \(d_n(0^n)=L_n+1\).

**3. Outputs with two ones.** Suppose the cyclic forward distance between their positions is \(d\in\{1,\ldots,n-1\}\). The two pairings have corridor lengths \(d-1\) and \(n-d-1\) respectively (with the zero-length corridor assigned weight \(F_0=0\)); therefore
\[
d_n(y)=F_{d-1}+F_{n-d-1}.
\]
If \(d=1\) or \(d=n-1\), this equals \(F_{n-2}\). Otherwise, put \(a=d-1\ge1\), \(b=n-d-1\ge1\), so \(a+b=n-2\ge5\). We prove \(F_a+F_b<F_{a+b}\). If \(a=1\), then \(b\ge4\) and \(F_{b+1}-F_b=F_{b-1}>1\), giving strictness; similarly if \(b=1\). If \(a,b\ge2\), the Fibonacci addition identity gives
\[
F_{a+b}=F_{a+1}F_b+F_aF_{b-1}\ge2F_b+F_a>F_b+F_a.
\]
Therefore only cyclically adjacent pairs attain \(F_{n-2}\) among outputs of weight two.

**4. Outputs with at least four ones.** Suppose \(y\) has \(2r\ge4\) ones. In any contributing pairing, the \(r\) long zero runs each use at least two sites, so the \(r\) positive corridor lengths satisfy \(T:=\sum_jt_j\le n-2r\). The Fibonacci addition identity
\[
F_{a+b-1}=F_aF_b+F_{a-1}F_{b-1}\quad(a,b\ge1)
\]
implies by induction that \(\prod_jF_{t_j}\le F_{T-r+1}\le F_{n-3r+1}\). (If \(n<3r\), no pairing contributes.) There are at most two pairings, hence
\[
d_n(y)\le2F_{n-3r+1}\le2F_{n-5}<F_{n-2}\qquad(n\ge7).
\]
The last strict inequality follows from \(F_{n-2}=2F_{n-4}+F_{n-5}\) and \(F_{n-4}\ge F_{n-5}>0\). Odd-weight positive outputs have no predecessor. Together with step 3 this proves the precise runner-up value and equality class. Finally \(L_n+1>F_{n-2}\), so all zero is the unique global maximizer. This concludes the proof for all \(n\ge7\).

## Verification
The standalone Python 3 program `verify.py` uses only the standard library. Execute `python3 verify.py` from the directory containing the file. It independently computes all fibers by direct enumeration of the \(2^n\) input configurations for every \(1\le n\le16\), compares every one of the \(131070\) output fibers with the pairing formula, and additionally compares with a four-state de Bruijn transfer-matrix trace for \(1\le n\le11\). It checks the exact maximum and all equality cases for \(7\le n\le16\), and prints `VERIFY_OK` on success. Direct computation tests small parameters; the proof above establishes the unbounded quantifiers.

The transfer matrices use states \(00,01,10,11\). With rows representing the incoming pair and columns the outgoing pair, the matrices for output zero and one respectively are
\[
M_0=\begin{pmatrix}1&0&0&0\\0&0&1&1\\0&1&0&0\\0&0&1&1\end{pmatrix},\quad
M_1=\begin{pmatrix}0&1&0&0\\0&0&0&0\\1&0&0&0\\0&0&0&0\end{pmatrix}.
\]
The identity \(d_n(y)=\operatorname{tr}(M_{y_0}\cdots M_{y_{n-1}})\) is a second independent finite-check method.

## Relationship to prior work
Jen's 1989 work provides general one-step preimage recurrences for finite output blocks on infinite lattices; it does not state a sharp second-largest fiber classification on indexed periodic Rule-18 rings. Powley's 2009 thesis studies Rule 18 and explicitly derives the homogeneous all-zero cyclic preimage count, an ingredient and a prior result here, but the inspected relevant chapter does not establish the maximization over **nonzero** outputs or its equality cases. Fukś's early paper (arXiv posting May 28, 2013, with a 2003 journal publication) examines preimage-sequence recurrences for elementary rules, not this output-wise modal optimization. The new contribution is the all-nonzero sharp comparison, complete adjacent-one equality class and pairing factorization; the known zero-fiber Lucas count is not claimed as new.

## Limitations
The result is confined to the one-step synchronous, indexed, cyclic binary Rule-18 map. It does not assert an entire fiber histogram, multi-step distribution, or optimality for other elementary rules. General historical recurrence methods may admit an unlocated equivalent formulation of the modal statement; independent priority checking remains worthwhile. The standalone computation is finite corroboration, not an infinite certificate.

## References
- Erica Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems 3 (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
- Edward Powley, *Global Properties of Cellular Automata*, PhD thesis, University of York, 2009, Chapter 9. https://edpowley.com/academic/papers/thesis.pdf
- Henryk Fukś, *Sequences of Preimages in Elementary Cellular Automata*, Complex Systems 14 (2003), 29–43; arXiv public posting May 28, 2013. https://arxiv.org/abs/1305.6533
