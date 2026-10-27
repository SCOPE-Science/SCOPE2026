# Sharp maximum size of a binary four-symbol cyclic-rotation error ball

## Finding
For every integer \(n\ge 4\), let \(B_4(x)\) contain a binary word \(x\in\{0,1\}^n\) and all distinct words obtained by cyclically rotating **exactly four consecutive coordinates** of \(x\) by one, two, or three places, with no wraparound. Then
\[
\max_{x\in\{0,1\}^n}|B_4(x)|=\left\lfloor\frac{11n-20}{5}\right\rfloor.
\]
For every \(n\ge4\), the length-\(n\) prefix of the infinite periodic binary word \(011100111001110\ldots\) attains equality.

## Assumptions and scope
The alphabet is binary, and indices range from \(0\) to \(n-1\). The channel makes at most one cyclic permutation of a contiguous **length-four** window; allowing a zero-error outcome is equivalent to including the center \(x\). A cyclic rotation is a rotation *within* the selected window, not a cyclic wraparound of the whole word. This result concerns neighborhood cardinalities, not an exact maximum size of an error-correcting code. In particular it is not a claim about the distinct channel that permits windows of lengths two, three, **or** four.

## Proof
For a length-\(n\) word \(x\), let \(E_i(x)\) be the set of nonidentity outputs obtained by rotating the window at positions \(i,i+1,i+2,i+3\), for \(0\le i\le n-4\). Every nonidentity output differs from \(x\) in at least two coordinates: rotation preserves the number of ones in the affected window, so a change at only one coordinate is impossible. If \(|i-j|\ge3\), the windows overlap in at most one coordinate; hence \(E_i(x)\cap E_j(x)=\varnothing\). It follows that
\[
|B_4(x)|=1+|E_0|+|E_1\setminus E_0|+
\sum_{i=2}^{n-4}|E_i\setminus(E_{i-1}\cup E_{i-2})|,
\]
with nonexistent terms omitted.

All three sorts of contributions are local. For binary strings \(z\) of lengths four, five, and six, respectively, write \(O_j(z)\) for the nonidentity outputs of the length-four window starting at \(j\), relative to the whole local string, and define
\[
F_0(z)=|O_0(z)|,\qquad
F_1(z)=|O_1(z)\setminus O_0(z)|,\qquad
R(z)=|O_2(z)\setminus(O_1(z)\cup O_0(z))|.
\]
Thus for \(n\ge5\), the contribution from the first five bits is \(F_0(x_0x_1x_2x_3)+F_1(x_0\cdots x_4)\), and each new bit contributes \(R\) applied to the last six bits. These are exact set identities, not probabilistic approximations.

Define \(v_n(s)\) as the maximum number of nonidentity ball outputs among length-\(n\) words ending in the five-bit suffix \(s\in\{0,1\}^5\). For \(n=5\),
\[
v_5(s)=F_0(s_0s_1s_2s_3)+F_1(s).
\]
For any four-bit word \(t\) and last bit \(b\), the exact recurrence is
\[
v_{n+1}(tb)=\max_{a\in\{0,1\}}
\bigl(v_n(at)+R(atb)\bigr),\qquad n\ge5,
\]
where \(atb\) is the six-bit concatenation. It exhausts all possible earlier prefixes because the local contribution needs only the preceding five bits.

Enumerate the 32 suffix states in lexicographic order. Exact set operations and the recurrence give the following vector at length six:

```text
v6 =
3 6 7 8 6 6 7 7 5 6 5 6 7 7 8 5
5 8 7 7 6 5 6 5 7 7 6 6 8 7 6 3
```

The same 32-state computation gives the **componentwise identity**
\[
v_{11}(s)=v_6(s)+11\quad\text{for every }s\in\{0,1\}^5.
\]
The attached self-contained checker verifies each entry of this equality both by the recurrence and by exhaustive full-word enumeration. Since the recurrence commutes with adding a constant to every state value, this identity propagates by induction:
\[
v_{n+5}(s)=v_n(s)+11\quad(n\ge6).
\]
The maximum ball sizes for \(n=4,5,6,7,8,9,10\) are, respectively, \(4,7,9,11,13,15,18\). These finitely established base values, together with the componentwise identity, yield the stated formula for every \(n\ge4\). This is an all-length proof because the 32-state recurrence represents every binary word; it is not an extrapolation from small \(n\).

For attainment, take the prefixes of the periodic word \(u=(01110)^\infty\). Its first window produces three nonidentity outputs; the second contributes three new outputs. Thereafter the successive local increments \(R\) repeat as \(2,2,2,2,3\), contributing eleven per five added positions. The length-four prefix has ball size four. Hence every prefix of length \(n\ge4\) attains precisely \(\lfloor(11n-20)/5\rfloor\).

## Verification
Run `python3 verify_cyclic4.py` with Python 3 and no external packages. The script constructs the local sets, builds the full 32-state recurrence, checks the pivotal componentwise five-step identity, and independently reconstructs all suffix-state maxima through length eleven by direct full-word enumeration. It checks the local decomposition for every binary word of lengths four through eleven and verifies the periodic witness through length one hundred. Expected final marker: `VERIFY_OK`.

## Relationship to prior work
Chen and Milenkovic introduce exactly the cyclic-substring permutation channel in Definition 3 of their October 2026 paper. Their Section III proves asymptotic redundancy lower bounds for window lengths at least nine; Section IV uses general local-window counting bounds. Their Example 1 treats one length-five input at window length four, and Section V identifies additional four-symbol error types without determining the maximum size of its error ball. The present statement gives a sharp all-length **exact-window-four** worst-case ball volume and an attaining periodic family, stronger for this fixed window than the immediate bound \(1+3(n-3)\) from counting three nontrivial rotations at each window position.

## Limitations
No classification of all maximizing center words is claimed. This does not determine the exact code-size optimum or the error-ball mean, and it does not apply unchanged to arbitrary four-symbol permutations, shorter window lengths, nonbinary alphabets, or multiple errors. Literature comparison is based on the primary text and accessible indexed searches; independently discovered unindexed equivalents remain possible. Independent audit has not been performed.

## References
1. Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, publicly posted 2026-10-11, especially Definition 3, Theorems 2–4, Example 1, and Section V. https://arxiv.org/html/2610.15701v1
