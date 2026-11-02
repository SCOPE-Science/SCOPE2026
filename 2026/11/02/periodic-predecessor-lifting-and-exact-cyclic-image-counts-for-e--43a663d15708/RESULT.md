# Periodic predecessor lifting and exact cyclic image counts for elementary cellular automaton Rule 126

## Finding
For each integer \(n\ge1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous Rule 126 update with all subscripts modulo \(n\). A nonconstant target \(y\) is in the image of \(F_n\) if and only if every cyclic maximal run of ones has length at least two and either one run has length at least four or the number of length-two one-runs is even. Additionally, \(0^n\) is always reachable and \(1^n\) is reachable exactly when \(n\ge2\). Thus cyclic avoidance of the previously known forbidden word `010` is sufficient for some periodic predecessor, but not always for a predecessor of the *same* period: any failed same-period case has a predecessor on the doubled ring and cannot have one on any odd positive multiple of the original period.

For every \(n\ge1\), write \(R_n=|\operatorname{Im}F_n|\). Define \(\tau_0=3\), \(\tau_1=\tau_2=2\), and \(\tau_n=2\tau_{n-1}-\tau_{n-2}+\tau_{n-3}\) for \(n\ge3\). Define Lucas numbers by \(L_0=2\), \(L_1=1\), and \(L_n=L_{n-1}+L_{n-2}\) for \(n\ge2\). Set \(\epsilon_n=2\cos(\pi n/2)\), and \(c_n=3(-1)^{n/3}\) if \(3\mid n\) and \(c_n=0\) otherwise. Then

\[
R_n=\tau_n-\frac{L_n+\epsilon_n-1-c_n}{2}-\mathbf1_{n=1}.
\]

The first 19 values, indexed by \(n=1,\ldots,19\), are `1, 2, 2, 6, 12, 23, 37, 66, 119, 217, 387, 693, 1237, 2207, 3927, 6986, 12412, 22028, 39047`. Furthermore, with \(p(z)=1-2z+z^2-z^3\) and \(b(z)=z^3(1+z)/(1-z)\), the **rational** ordinary generating function is

\[
\sum_{n\ge1}R_nz^n=-\frac{zp'(z)}{p(z)}-\frac{zb'(z)}{2(1-b(z))}-\frac{3z^3}{2(1+z^3)}-z.
\]

If \(\lambda\) is the positive real root of \(t^3-2t^2+t-1=0\), and \(\varphi=(1+\sqrt5)/2\), then

\[
R_n=\lambda^n-\frac12\varphi^n+O(1),\qquad \lambda\approx1.75487766624669.
\]

## Assumptions and scope
Binary words have **indexed** cyclic coordinates; rotations are counted separately. Rule 126 outputs one on exactly the neighborhoods `001`, `010`, `011`, `100`, `101`, `110`, and zero on `000`, `111`. A cyclic factor or run is interpreted on the infinite periodic repetition, including degenerate rings of lengths one and two. A predecessor of period \(n\) means an \(n\)-indexed ring configuration, whose least period is allowed to divide \(n\). The periodic-lifting multiplier \(k\) asks for a predecessor on the repeated target \(y^k\), considered as a word of length \(kn\); it does not require a primitive period. No noise or more than one time update is considered.

## Proof
**1. Binary-boundary factorization.** For an input \(x\), define \(d_i=x_i\oplus x_{i+1}\). Direct examination of the two zero-output and six one-output neighborhoods gives

\[
(F_n(x))_i=d_{i-1}\lor d_i.
\]

Around a cyclic ring the XOR of the boundary values equals zero, so \(\sum_{i=0}^{n-1}d_i\equiv0\pmod 2\). Conversely, for every even-weight cyclic sequence \(d\), fix \(x_0\in\{0,1\}\) and integrate \(x_{i+1}=x_i\oplus d_i\). This returns to the selected \(x_0\) and constructs precisely two possible \(n\)-ring inputs. Consequently the image question is equivalent to existence of an even-weight \(d\) with \(y_i=d_{i-1}\lor d_i\).

**2. Output runs and parity.** An output zero forces both adjacent boundary values to zero. Consequently the cyclic output pattern `010` cannot occur. If the output is nonconstant and avoids `010`, each maximal one-run has length \(\ell\ge2\). On the \(\ell\)-symbol run, the two boundary values just outside the run are zero, and the \(\ell-1\) internal boundary values must begin and end with one and contain no adjacent zeros. For \(\ell=2\), the only interior is `1` and contributes odd parity. For \(\ell=3\), it is `11` and contributes even parity. For every \(\ell\ge4\), the assignment with all internal values one and the assignment with exactly one interior zero (not at either end) are both valid and have opposite parity. Distinct one-runs are separated by forced zeros, so their choices are independent. This proves the stated criterion: parity can be corrected whenever a run has length at least four, and otherwise the forced parity is the parity of the number of length-two runs. The all-zero output is obtained from \(d=0^n\) for any \(n\). For the all-one output, when \(n\ge2\) choose any boundary pattern with no consecutive zeros and even weight: all ones if \(n\) is even, or exactly one zero if \(n\) is odd and at least three; when \(n=1\), the only even-weight boundary pattern is zero, so output one is impossible.

**3. Sharp period lifting.** For a cyclic output avoiding `010` but failing the same-period parity test, the preceding construction yields a boundary assignment with *odd* parity and the prescribed output, because all run interiors are forced; for the special \(n=1\), take boundary symbol one. Repeating this boundary assignment twice produces even total parity and hence an input on the \(2n\)-ring. For a general positive multiple \(kn\), the forced interior assignment repeats \(k\) times for the parity-obstructed outputs, so total parity equals \(k\pmod2\). Thus exactly even multipliers permit predecessors; no odd multiplier does. An output containing `010` cannot be produced at any multiplier. In particular \((011)^{2j+1}\) for every integer \(j\ge0\) gives an infinite family where one period fails and two periods work.

**4. Count `010`-avoiding indexed cyclic words.** Form the four-state overlap matrix on states `00`, `01`, `10`, `11`, recording permissible triples:

```
T = [[1,1,0,0],
     [0,0,0,1],
     [1,1,0,0],
     [0,0,1,1]]
```

Closed walks of length \(n\) correspond bijectively to indexed cyclic binary words avoiding `010`, including small rings. Thus their number is \(A_n=\operatorname{tr}(T^n)\). Direct determinant expansion gives \(\det(I-zT)=1-2z+z^2-z^3=p(z)\), and therefore \(\sum_{n\ge1}A_nz^n=-zp'(z)/p(z)\). Newton identities yield \(A_n=\tau_n\) as defined above (the fourth eigenvalue is zero and does not contribute for positive \(n\)).

**5. Count precisely the parity-obstructed outputs.** Apart from the all-one word of length one, the candidates that avoid `010` but might fail the parity test are the *nonconstant* cyclic words whose every one-run has length two or three. Every such word is a cyclic concatenation of blocks consisting of a nonempty zero-run followed by a one-run of length two or three. The block length enumerator is

\[
b(z)=\Bigl(\frac z{1-z}\Bigr)(z^2+z^3)=\frac{z^3(1+z)}{1-z}.
\]

If there are \(m\) blocks in an indexed word of total length \(n\), marking an index among its \(n\) sites rather than one of its \(m\) block starts changes the coefficient by a factor \(n/m\). Consequently the ordinary generating function for the number \(B_n\) of such indexed cyclic words is \(\sum_{n\ge1}B_nz^n=zb'(z)/(1-b(z))\). This identity counts periodic words correctly because the number of marked block starts among \(n\) indexed positions is \(m\) even when the word has rotational symmetry.

Since

\[
1-b(z)=\frac{(1+z^2)(1-z-z^2)}{1-z},
\]

taking logarithmic derivatives shows \(B_n=L_n+\epsilon_n-1\), with \(\epsilon_n=2\cos(\pi n/2)\). Weight each word by \((-1)^{q}\), where \(q\) is the number of its length-two one-runs. Changing the weight of a length-two block from \(+1\) to \(-1\) replaces the block enumerator by

\[
\widetilde b(z)=\frac z{1-z}(-z^2+z^3)=-z^3.
\]

Therefore the signed count \(C_n\) has series

\[
\sum_{n\ge1}C_nz^n=\frac{z\widetilde b'(z)}{1-\widetilde b(z)}=-\frac{3z^3}{1+z^3},
\]

hence \(C_n=c_n\) from the theorem. The number of odd-parity candidates is \((B_n-C_n)/2\). Every other `010`-avoider is reachable, except the length-one all-one word. Subtracting these from \(A_n=\tau_n\) proves the exact count and stated rational generating function.

**6. Growth.** The characteristic polynomial of the nonzero eigenvalues of \(T\) is \(t^3-2t^2+t-1\). It has one real root \(\lambda>\varphi\) and a complex-conjugate pair whose moduli are \(\lambda^{-1/2}<1\), since their product with \(\lambda\) is one. Thus \(\tau_n=\lambda^n+O(1)\). The Lucas identity \(L_n=\varphi^n+(-1/\varphi)^n\), together with bounded periodic terms \(\epsilon_n\) and \(c_n\), proves the asymptotic formula.

## Verification
`verify.py` is a standalone Python 3 standard-library checker. Run `python3 verify.py`; the expected terminal line is `VERIFY_OK`. It evaluates Rule 126 directly from its neighborhood truth table, independently enumerates every input ring and candidate output ring for lengths \(1\) through \(18\), compares the run criterion and closed formula, independently enumerates the signed short-run class through length \(15\), checks the transfer-matrix recurrence through length \(120\), and constructs lifts on length \(n\) or \(2n\) through length \(13\). Its successful replay is a finite reproducibility check; the preceding all-length arguments, not the finite computation, establish the theorem. The first 19 exact image counts are stated above for reproducibility.

## Relationship to prior work
The local Rule-126 truth table and its long-established symbolic dynamics are classical. McIntosh's `010` Garden-of-Eden factor is specifically reported in Martínez et al., *How to make dull cellular automata complex by adding memory: Rule 126 case study* (2010; openly available as arXiv:1212.0124v1, submitted 2012-12-01). That paper discusses finite periodic basins (through ring length 18) and de Bruijn representations but does not in the inspected text give the precise parity obstruction, sharp period doubling or all-length image enumeration above. OEIS A269173 independently records a bitwise XOR/OR formula for the local rule, which is therefore **not** claimed as new. The novel contribution proposed here is the *global same-period image classification and its enumeration*, not the local identity or the forbidden word alone. The full 2009 McIntosh monograph and some historical accounts were unavailable for complete page-by-page comparison, so priority remains provisional.

## Limitations
The formula counts indexed targets, not binary necklaces or dihedral equivalence classes. It is a one-step synchronous result for Rule 126 with periodic boundary conditions; it does not describe multistep images, predecessor multiplicities for each target, or noisy outputs. Finite tests do not constitute all-length proof. The historical originality assessment is based on the cited accessible literature and may be revised if inaccessible material proves stronger.

## References
1. Martínez, G. J., Adamatzky, A., Seck-Tuoh-Mora, J. C., and Alonso-Sanz, R., *How to make dull cellular automata complex by adding memory: Rule 126 case study*, *Complexity* **15**(6), 34–49 (2010); publicly available version `arXiv:1212.0124v1` (2012-12-01), https://arxiv.org/html/1212.0124v1 .
2. McIntosh, H. V., *One Dimensional Cellular Automata* (2009), cited for Rule-126 de Bruijn/subset analysis by Reference 1. Full text not inspected.
3. OEIS Foundation, sequence `A269173`, local bitwise Rule-126 map, https://oeis.org/A269173 (first listed 2016-02-22).
4. Wolfram, S., *Statistical Mechanics of Cellular Automata*, *Reviews of Modern Physics* **55** (1983), 601–644; https://mathworld.wolfram.com/Rule126.html .
