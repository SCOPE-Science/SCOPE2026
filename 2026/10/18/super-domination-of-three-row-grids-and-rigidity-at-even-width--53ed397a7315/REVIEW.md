# Independent mathematical audit

## correctness

PASS

Definition requires each omitted vertex to have a selected witness whose open neighbourhood contains exactly that omitted vertex. Encoding omitted row triples as masks makes each test depend on the five-column window centered on its column, with virtual zeros and forbidden out-of-grid witnesses at boundaries. A complete max-plus DP on ordered quadruples of column masks stores largest omitted counts; its full vectors, not only terminal maxima, satisfy V11=V9+3 and V12=V10+3 on identical 1543-state supports. Since subsequent transfer and terminal two zero-column closures are stationary and additively homogeneous, the recurrence extends to ALL n>=9, independent of extrapolated finite pattern. Exact n=1..12 bases are 2,3,5,6,9,9,12,12,15,15,18,18. I independently reimplemented state transitions and checked 1..14, supports 1543, full vector equalities for (9,11),(10,12),(11,13),(12,14); direct unrelated exhaustive witness enumeration at n=1..6 gives minima counts 3,2,4,2,60,2. Even n equality |D|=half vertices forces a matching across the cut; square parity propagates horizontal or vertical crossing lines, vertical perfect matching impossible with odd three rows, so alternating full columns and exactly two assignments. Numerical even case was already known from Klein et al; the checked additions are odd exactness and rigidity.

## originality

PASS

Theorem24 of Klein, Rodríguez-Velázquez and Yi (2017) establishes the even-product half-order value and bounds for odd widths, so it already covers the even numerical formula. It does not supply exact odd n>=5 or unique two alternating min sets. Ghanbari–Jäger–Lehtilä (2022/2024) discuss classes and enumerations, not this exact 3-row full all-width grid and rigidity theorem in inspected relevant parts.

## value

PASS

Sharp odd-width profile closes an explicit interval between pre-existing lower and upper bounds, with genuine exceptional width n=3. The complete equality-case rigidity for even grids gives useful structure beyond known half-size values. Exact finite-state all-width induction makes a natural infinite family fully resolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
