# Exact fiber and constant-weight capacity laws for cyclic binary weighted reads

## Finding
Fix integers \(n\ge2\) and \(1\le\ell\le n\). An indexed cyclic binary source is \(x=(x_0,\ldots,x_{n-1})\in\{0,1\}^n\), with coordinates indexed modulo \(n\). Its complete cyclic sliding-weight read vector is
\[
R_\ell(x)_i=\sum_{j=0}^{\ell-1}x_{i+j}\quad(0\le i<n),
\]
where sums are over the integers. Put \(d=\gcd(n,\ell)\), \(L=n/d\), and \(m=2^L-2\).

**Exact inverse fibers.** Partition the coordinates into their \(d\) labeled residue classes modulo \(d\), each of length \(L\). Call a class *pure* when all its bits agree and *mixed* otherwise. Two sources have the same complete read vector if and only if they agree on every mixed class and have the same number of pure classes equal to one. Consequently a read vector with \(p\) pure classes, of which \(h\) are all-one, has exactly \(\binom ph\) preimages; its \(d-p\) mixed classes are fixed. For every positive integer \(k\), the number of attainable read vectors with exactly \(k\) preimages is
\[
N_k(n,\ell)=\sum_{p=0}^{d}\binom dp(2^L-2)^{d-p}
\sum_{h=0}^{p}\mathbf1_{\{\binom ph=k\}}.
\]

**Exact optimal zero-error code size.** There are precisely
\[
A_{n,\ell}=(2^L-1)^{d-1}(2^L+d-1)
\]
attainable indexed read vectors, hence this is the maximum size of a binary length-\(n\) code distinguishable by the noiseless cyclic read channel. The number of singleton fibers is
\[
S_{n,\ell}=2(2^L-1)^d-(2^L-2)^d.
\]
The channel is injective on all binary words exactly when \(\gcd(n,\ell)=1\). For \(d\ge2\), the largest inverse list has size \(\binom d{\lfloor d/2\rfloor}\); exactly one constant read vector attains it when \(d\) is even, and exactly two constant read vectors attain it when \(d\) is odd.

**Exact constant-weight capacity.** For each \(0\le w\le n\), let \(A_{n,\ell,w}\) be the number of attainable read vectors arising from binary sources of weight \(w\), equivalently the optimal zero-error code cardinality restricted to that weight. The following is an identity of polynomials (the apparent quotient is removable):
\[
\boxed{\sum_{w=0}^{n}A_{n,\ell,w}z^w
=\frac{\bigl((1+z)^L-z^L\bigr)^d-z^L\bigl((1+z)^L-1\bigr)^d}{1-z^L}.}
\]
For fixed \(L\ge2\), along the lengths \(n=Ld\) and windows \(\ell=rd\) with \(1\le r<L\) and \(\gcd(L,r)=1\), the exact code rate satisfies
\[
\lim_{d\to\infty}\frac{\log_2 A_{Ld,rd}}{Ld}=\frac{\log_2(2^L-1)}{L}<1.
\]
In contrast, for a fixed window length \(\ell\), \(A_{n,\ell}/2^n\to1\) as \(n\to\infty\). Thus an arithmetic alignment of window and cycle lengths produces a genuine finite-rate loss absent for coprime lengths.

## Assumptions and scope
The source coordinates and output coordinates are indexed: rotations are **not** identified, and the order of read sums is retained. Each read wraps around the circular boundary. The binary alphabet is exactly \(\{0,1\}\), observations are uncorrupted integer Hamming weights, and every one of the \(n\) cyclic starting positions is observed. The read window has length between one and the cycle length inclusive. The weight of a source is \(\sum_i x_i\). The case \(\ell=n\) is allowed and produces a constant read vector equal to the full source weight; the case \(\ell=1\) reproduces the source exactly. These formulas do not concern an unindexed multiset of read weights or a noncyclic, zero-padded read channel.

## Proof
For two sources \(x,x'\), write \(a_i=x'_i-x_i\). Adjacent output differences satisfy the exact integer identity
\[
R_\ell(x)_{i+1}-R_\ell(x)_i=x_{i+\ell}-x_i.
\]
If the outputs agree, subtraction shows \(a_{i+\ell}=a_i\) at every position. The map \(i\mapsto i+\ell\pmod n\) traverses each residue class modulo \(d\) in one cycle of length \(L\), so \(a\) is constant on each of these classes. Conversely, if its class constants are \(a_0,\ldots,a_{d-1}\), then every window of length \(\ell\) contains precisely \(\ell/d\) positions from each class, and therefore
\[
R_\ell(x')_i-R_\ell(x)_i=\frac{\ell}{d}\sum_{r=0}^{d-1}a_r
\]
independently of \(i\). Thus the two output vectors agree **if and only if** the differences are class-constant and their \(d\) class constants sum to zero.

If a class of \(x\) contains both a zero and a one, adding an integer constant while keeping all its entries binary forces that constant to be zero. If the class is all zero, its allowed constants are zero and one; if it is all one, they are zero and minus one. Hence mixed classes remain fixed, while a pure all-zero class may change to all-one precisely when another pure all-one class changes to all-zero. The sum-zero condition is exactly conservation of the number \(h\) of pure all-one classes. All \(\binom ph\) choices are feasible and indistinguishable, proving the complete inverse-fiber classification.

Choose which \(p\) of the \(d\) classes are pure. Every mixed class permits \(m=2^L-2\) different binary patterns, while the pure classes give one distinct output for each choice \(h=0,\ldots,p\), not one per choice of which classes are one. Therefore the number of output classes with a specified pair \((p,h)\) is \(\binom dp m^{d-p}\), and the stated \(N_k\) formula follows. Summing over \(h\) and \(p\) yields
\[
A_{n,\ell}=\sum_{p=0}^d\binom dp m^{d-p}(p+1)
=(m+1)^d+d(m+1)^{d-1}.
\]
A fiber is a singleton exactly when \(p=0\), or \(p\ge1\) and \(h\in\{0,p\}\). Including the \(p=0\) case only once gives \(S_{n,\ell}=2(m+1)^d-m^d\). If \(d=1\) all fibers are singleton. If \(d\ge2\), setting any two residue classes to pure opposite bits exhibits a collision. Since \(\binom ph\le\binom d{\lfloor d/2\rfloor}\), with equality for \(d\ge2\) only at \(p=d\) and central \(h\), the maximum and its one-or-two all-constant read-vector extremizers follow. All-pure sources are \(d\)-periodic and each cyclic window has constant value \((\ell/d)h\).

For the weight refinement, a fixed mixed class contributes \(\binom Ls\) available patterns of weight \(s\) for \(1\le s<L\). Let \(M(z)=\sum_{s=1}^{L-1}\binom Ls z^s=(1+z)^L-1-z^L\). With \(p\) pure classes and \(h\) all-one, every represented output has source weight \(Lh\) plus the mixed-class weights. Thus
\[
\sum_{w=0}^n A_{n,\ell,w}z^w
=\sum_{p=0}^d\binom dp M(z)^{d-p}\sum_{h=0}^p z^{Lh}.
\]
Applying the finite geometric identity to the inner sum gives
\[
\frac{(M(z)+1)^d-z^L(M(z)+z^L)^d}{1-z^L},
\]
which is the displayed polynomial. Each fiber has one fixed source weight because the output sum equals \(\ell\) times the source weight, so counting outputs at weight \(w\) is exactly constant-weight zero-error capacity. A code attaining each capacity chooses one canonical source for every output (for example, retain all mixed classes and fill the first \(h\) pure residue classes with ones).

Finally, substituting \(n=Ld\) and \(\ell=rd\) with \(\gcd(L,r)=1\) into the exact capacity gives the stated limiting rate. If \(\ell\) is fixed and \(n\to\infty\), then \(d\le\ell\) and \(L\to\infty\); dividing the exact capacity by \(2^{Ld}\) shows convergence to one. No asymptotic approximation is used in the exact formulas.

## Verification
The standalone `verify.py` computes every indexed circular read vector literally, independently implements the binomial-fiber histogram and the constant-weight polynomial as exact integer sums, and compares all formulas for every \(2\le n\le14\) and \(1\le\ell\le n\). It also checks the capacity, singleton count, maximum fiber and source-mass conservation. In the smaller range \(2\le n\le8\), it reconstructs all source words from each output using an independently implemented inverse algorithm based on cyclic first differences.

Run with `python3 verify.py`. The recorded execution was `VERIFY_OK source_words= 425984 profiles= 381082 inverse_cases= 3036 all_n=2..14 all_ell=1..n`. The counts reflect repeated enumeration of the same source length at different window lengths. The finite checks corroborate the proof and do not establish its universal quantifiers by themselves.

For a concrete resonant case, \(n=12\), \(\ell=6\), \(d=6\), \(L=2\): exactly \(2187\) read vectors are attainable; \(1394\) have one source; the largest list has \(20\) sources. For comparison, at \(n=12\), \(\ell=5\), all \(4096\) sources have distinct read vectors because the lengths are coprime.

## Relationship to prior work
Chee, Vardy, Vu and Yaakobi introduced the transverse-read model and explicitly note that a cyclic version is possible but restrict their 2021 and 2023 treatments to the noncyclic segment-read channel; in particular, their finite-state and asymptotic-capacity results do not supply the residue-class inverse fibers or fixed-weight cyclic capacity here. Yerushalmi, Etzion and Yaakobi (arXiv:2401.15368v1) analyze the **noncyclic** weighted-read channel for general shift sizes and determine several asymptotic capacities. Its aligned-window setting is the mathematical motivation, not a statement of the cyclic theorem. Banerjee and collaborators (arXiv:2401.15939v1) use a *zero-padded linear* read vector that is injective without noise, in contrast with the cyclic resonances analyzed here.

Levinson and Markel (arXiv:2011.10130v2, first posted in 2020) study inversion from selected low-frequency DFT coefficients of binary vectors. Their Fourier sampling mask differs from the zeros of a circular boxcar convolution, and their results establish uniqueness criteria rather than the complete count of integer-weighted window-sum outputs or their constant-weight fibers.

The closest published calculation located for a related read channel is the exact maximum-fiber law for the noncyclic binary \((3,2)\) transverse read vector, which yields a Fibonacci quantity; its windows start two positions apart and stop at an endpoint, while here *all* circular unit-shift windows are retained. The prior binary cyclic substring-composition profiles record unordered histograms of read weights or factor counts, rather than the ordered vector of \(n\) aligned weights used here. Neither observation model determines this exact fiber classification. Searches for the formula, the residue-class alias, cyclic convolution, finite weighted-read capacity, and fixed-composition equivalences found no identified statement implying the theorem. This is evidence for originality, not proof of priority; an equivalent unindexed circulant-convolution or tomography result remains possible.

## Limitations
The theorem requires a known cyclic coordinate origin and complete noiseless read vectors. It does not give capacities for unknown rotations, missing read positions, corrupted weights, general nonbinary symbol-sum observations, or arbitrary shift sizes. The model is a mathematically natural circular counterpart of a physical linear read device, not a direct claim about the behavior of a specific sequencer. Earlier unpublished or differently indexed results could contain an equivalent circulant-sum count. The standalone finite check uses ordinary enumeration and does not serve as an independent research audit.

## References
1. O. Yerushalmi, T. Etzion, and E. Yaakobi, *The Capacity of the Weighted Read Channel*, arXiv:2401.15368v1, first public 2024-01-27, https://arxiv.org/abs/2401.15368.
2. Y. M. Chee, A. Vardy, V. K. Vu, and E. Yaakobi, *Coding for Transverse-Reads in Domain Wall Memories*, IEEE ISIT 2021, DOI:10.1109/ISIT45174.2021.9518271.
3. Y. M. Chee, A. Vardy, V. K. Vu, and E. Yaakobi, *Transverse-Read-Codes for Domain Wall Memories*, IEEE Journal on Selected Areas in Information Theory 4 (2023), pp. 784–793, DOI:10.1109/JSAIT.2023.3334303, https://ymchee66.github.io/home/PDF/transverse-readj.pdf.
4. A. Banerjee, Y. Yehezkeally, A. Wachter-Zeh, and E. Yaakobi, *Correcting a Single Deletion in Reads from a Nanopore Sequencer*, arXiv:2401.15939v1, first public 2024-01-29, https://arxiv.org/abs/2401.15939.
5. H. W. Levinson and V. A. Markel, *Binary Discrete Fourier Transform and its Inversion*, arXiv:2011.10130v2, first public 2020-11-19, https://arxiv.org/abs/2011.10130.
