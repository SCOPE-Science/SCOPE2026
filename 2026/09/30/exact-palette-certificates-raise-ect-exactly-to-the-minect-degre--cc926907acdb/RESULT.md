# Exact palette certificates raise ECT exactly to the minECT degree
## Finding
Let \(k\geq 1\) and let \(f:\mathbb N\to k\) be a finite coloring. Write
\[
\operatorname{Inf}(f)=\{i<k:\{n:f(n)=i\}\text{ is infinite}\}.
\]
The eventually constant palette tail problem \(\mathrm{ECT}\) asks for any \(b\in\mathbb N\) such that
\[
\forall x\geq b\ \exists y>x\quad f(y)=f(x).
\]
Let \(\mathrm{CB}\) ask for the exact set \(\operatorname{Inf}(f)\). Define the palette-certified problem \(\mathrm{PECT}\) to return both an \(\mathrm{ECT}\)-bound \(b\) and \(\operatorname{Inf}(f)\) for the same input coloring.

Then
\[
\mathrm{PECT}\equiv_{\mathrm{sW}}\mathrm{ECT}\times\mathrm{CB}.
\]
Moreover,
\[
\mathrm{CB}\equiv_{\mathrm{sW}}\mathrm{isInfinite}^{*},
\]
where \(\mathrm{isInfinite}\) maps a binary sequence to \(1\) exactly when it has infinitely many \(1\)'s, and \(^{*}\) denotes finite parallelization. Therefore, using the known equivalences
\[
\mathrm{ECT}\equiv_{\mathrm W}\mathrm{TC}_{\mathbb N}^{*}
\quad\text{and}\quad
\mathrm{minECT}\equiv_{\mathrm W}\mathrm{TC}_{\mathbb N}^{*}\times\mathrm{isInfinite}^{*},
\]
one obtains
\[
\mathrm{PECT}\equiv_{\mathrm W}\mathrm{minECT}.
\]
Since \(\mathrm{ECT}<_{\mathrm W}\mathrm{minECT}\), it follows that
\[
\mathrm{ECT}<_{\mathrm W}\mathrm{PECT}.
\]

Thus augmenting an arbitrary valid \(\mathrm{ECT}\) bound with the exact set of colors recurring infinitely often raises the ordinary Weihrauch degree by exactly the same amount as demanding the least valid \(\mathrm{ECT}\) bound.

## Assumptions and scope
Inputs use the standard finite-coloring representation: a positive integer \(k\) and an oracle for \(f:\mathbb N\to k\). Products are the usual Weihrauch products, and strong Weihrauch reducibility is used where displayed.

For \(\mathrm{isInfinite}^{*}\), the input is any finite tuple of binary sequences, including the empty tuple. For \(\mathrm{CB}\), the color set is nonempty. The proof allows unused colors in a finite palette.

The comparison with \(\mathrm{minECT}\) uses the first-order Weihrauch results for \(\mathrm{ECT}\) and \(\mathrm{minECT}\) proved by Davis, Hirschfeldt, Hirst, Pardo, Pauly, and Yokoyama.

## Proof
First,
\[
\mathrm{CB}\leq_{\mathrm{sW}}\mathrm{isInfinite}^{*}.
\]
Given \(f:\mathbb N\to k\), for every \(i<k\) form the binary sequence
\[
p_i(n)=
\begin{cases}
1,&f(n)=i,\\
0,&f(n)\neq i.
\end{cases}
\]
The \(\mathrm{isInfinite}\) answer for \(p_i\) is \(1\) exactly when \(i\in\operatorname{Inf}(f)\). The finite tuple of answers therefore determines \(\operatorname{Inf}(f)\) without further access to \(f\).

Conversely,
\[
\mathrm{isInfinite}^{*}\leq_{\mathrm{sW}}\mathrm{CB}.
\]
Suppose the input consists of \(m\) binary sequences \(p_0,\ldots,p_{m-1}\). Construct a finite coloring \(h\) in blocks of length \(m+1\). Put the marker color
\[
M=3m
\]
at the first position of every block. At the \(i\)-th remaining position of block \(t\), put
\[
h((m+1)t+i+1)=
\begin{cases}
3i+1,&p_i(t)=1,\\
3i+2,&p_i(t)=0.
\end{cases}
\]
Use any finite palette large enough to contain these values. The unique infinitely recurring color divisible by \(3\) is \(M\), so \(m=M/3\) is recoverable from the color basis alone. For each \(i<m\),
\[
3i+1\in\operatorname{Inf}(h)
\quad\Longleftrightarrow\quad
p_i\text{ has infinitely many }1\text{'s}.
\]
Hence the whole finite tuple of \(\mathrm{isInfinite}\) answers is recoverable from the \(\mathrm{CB}\) output, establishing the strong reduction. When \(m=0\), the construction consists only of the marker color \(0\), and the same decoding gives the empty answer tuple.

Next,
\[
\mathrm{PECT}\leq_{\mathrm{sW}}\mathrm{ECT}\times\mathrm{CB}
\]
by sending the same coloring to both factors and returning the two outputs.

For the reverse strong reduction, start with independent inputs \(f:\mathbb N\to k\) for \(\mathrm{ECT}\) and \(h:\mathbb N\to\ell\) for \(\mathrm{CB}\), where \(k,\ell\geq 1\). Encode both into one coloring \(g\) using blocks of length \(3\):
\[
g(3t)=4\ell,
\qquad
g(3t+1)=4f(t)+1,
\qquad
g(3t+2)=4h(t)+2.
\]
Choose any finite codomain containing these values. Suppose \(\mathrm{PECT}(g)\) returns a valid tail bound \(b\) and the persistent palette \(S=\operatorname{Inf}(g)\).

The unique member of \(S\) congruent to \(0\pmod 4\) is the marker \(4\ell\), so \(\ell\) is recoverable from \(S\). The color basis of \(h\) is then
\[
\operatorname{Inf}(h)=\{j<\ell:4j+2\in S\}.
\]
For the \(\mathrm{ECT}\) component, set
\[
B=\left\lfloor\frac{b+1}{3}\right\rfloor.
\]
If \(x\geq B\), then \(3x+1\geq b\). Validity of \(b\) for \(g\) gives a later occurrence of the color \(g(3x+1)\). Because only positions congruent to \(1\pmod 3\) carry colors congruent to \(1\pmod 4\), this later occurrence has the form \(3y+1\) with \(y>x\), and therefore \(f(y)=f(x)\). Thus \(B\) is a valid \(\mathrm{ECT}\)-bound for \(f\). Both requested outputs are reconstructed solely from \((b,S)\), so
\[
\mathrm{ECT}\times\mathrm{CB}\leq_{\mathrm{sW}}\mathrm{PECT}.
\]

Combining the strong factorization with
\[
\mathrm{CB}\equiv_{\mathrm{sW}}\mathrm{isInfinite}^{*}
\]
and the known ordinary Weihrauch identities
\[
\mathrm{ECT}\equiv_{\mathrm W}\mathrm{TC}_{\mathbb N}^{*},
\qquad
\mathrm{minECT}\equiv_{\mathrm W}\mathrm{TC}_{\mathbb N}^{*}\times\mathrm{isInfinite}^{*},
\]
gives
\[
\mathrm{PECT}\equiv_{\mathrm W}\mathrm{minECT}.
\]
The known strict inequality \(\mathrm{ECT}<_{\mathrm W}\mathrm{minECT}\) yields the final strictness statement.

## Verification
The reductions were reconstructed with their strong postprocessing requirements checked explicitly. In the \(\mathrm{isInfinite}^{*}\)-to-\(\mathrm{CB}\) reduction, the number \(m\) of input sequences is encoded by the unique persistent color divisible by \(3\). In the product-to-\(\mathrm{PECT}\) reduction, the second palette size \(\ell\) is encoded by the unique persistent color divisible by \(4\). Thus neither postprocessor needs access to the original input.

The bound conversion
\[
B=\left\lfloor\frac{b+1}{3}\right\rfloor
\]
was checked against all residue classes of \(b\) modulo \(3\). It guarantees \(3x+1\geq b\) whenever \(x\geq B\).

The included `verify.py` exhaustively tests the tagging constructions on small ultimately periodic binary and finite colorings. It verifies the persistent-palette decoding and the transfer of every tested valid tail bound from the combined coloring back to the first coloring. The script terminates with `VERIFY_OK`.

## Relationship to prior work
Davis, Hirschfeldt, Hirst, Pardo, Pauly, and Yokoyama introduced and analyzed the eventually constant palette tail principle in Weihrauch terms. They proved
\[
\mathrm{ERT}\equiv_{\mathrm W}\mathrm{LPO}^{*}
<_{\mathrm W}
\mathrm{TC}_{\mathbb N}^{*}
\equiv_{\mathrm W}
\mathrm{ECT},
\]
and later in the same work proved
\[
\mathrm{minECT}\equiv_{\mathrm W}\mathrm{TC}_{\mathbb N}^{*}\times\mathrm{isInfinite}^{*}
\]
together with
\[
\mathrm{ECT}<_{\mathrm W}\mathrm{minECT}.
\]

A later color-basis study by Davis, Hirst, Keohulian, Miller, and Ross considers the exact set of colors occurring infinitely often. The present result links these two directions by showing that attaching that exact palette to an arbitrary \(\mathrm{ECT}\) witness has a strong product factorization and has, at the ordinary Weihrauch level, exactly the \(\mathrm{minECT}\) degree.

## Limitations
The strong equivalence proved here is
\[
\mathrm{PECT}\equiv_{\mathrm{sW}}\mathrm{ECT}\times\mathrm{CB}.
\]
The subsequent identification with \(\mathrm{minECT}\) is asserted only for ordinary Weihrauch reducibility, because the cited decomposition of \(\mathrm{minECT}\) is an ordinary Weihrauch equivalence.

The theorem concerns finite colorings of \(\mathbb N\). It does not claim an analogous factorization for higher-order color-basis principles, infinite color sets, or representations in which the finite palette size is unavailable.

The originality assessment is best-of-knowledge. Targeted checks located the separate \(\mathrm{ECT}/\mathrm{minECT}\) decomposition and the later color-basis line, but did not locate the combined palette-certified factorization stated here.

## References
Caleb Davis, Denis R. Hirschfeldt, Jeffry L. Hirst, Jake Pardo, Arno Pauly, and Keita Yokoyama, “Combinatorial principles equivalent to weak induction,” arXiv:1812.09943v1, 24 December 2018.

Caleb Davis, Jeffry L. Hirst, Asher Keohulian, Russell Miller, and Reed Solomon Ross, “Reverse mathematics of a color basis theorem,” preprint dated 10 November 2024; later published in *Computability* 14(2), DOI:10.1177/22113568241304637.
