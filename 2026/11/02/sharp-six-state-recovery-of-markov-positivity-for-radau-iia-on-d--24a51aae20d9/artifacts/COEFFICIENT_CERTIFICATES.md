# Rational coefficient certificates

The row-generator is \(Q_n=S_n-I_n\), and for \(n=2,3,4,5,6\),
\[R(hQ_n)=\frac{\sum_{j=0}^{n-1}N_{n,j}(h)S_n^j}{D_n(h)}.\]

These are exact integer-polynomial identities obtained by reducing the quadratic denominator modulo \(S_n^n=I_n\). Each is checked independently by `verify_radau_cycle.py`.

## Dimension 2

\[D_{2}(h)=2 h^{2} + 4 h + 3.\]

\[N_{2,0}(h)=h^{2} + h + 3.\]

\[N_{2,1}(h)=h \left(h + 3\right).\]

## Dimension 3

\[D_{3}(h)=3 h^{4} + 12 h^{3} + 22 h^{2} + 24 h + 12.\]

\[N_{3,0}(h)=h^{4} + 2 h^{3} + 4 h^{2} + 12 h + 12.\]

\[N_{3,1}(h)=h \left(h^{3} + 4 h^{2} + 12 h + 12\right).\]

\[N_{3,2}(h)=h^{2} \left(h^{2} + 6 h + 6\right).\]

## Dimension 4

\[D_{4}(h)=\left(4 h^{2} + 8 h + 6\right) \left(h^{4} + 4 h^{3} + 8 h^{2} + 12 h + 9\right).\]

\[N_{4,0}(h)=h^{6} + 3 h^{5} + 3 h^{4} + 19 h^{3} + 63 h^{2} + 90 h + 54.\]

\[N_{4,1}(h)=h \left(h^{5} + 5 h^{4} + 22 h^{3} + 63 h^{2} + 90 h + 54\right).\]

\[N_{4,2}(h)=h^{2} \left(h^{4} + 7 h^{3} + 27 h^{2} + 45 h + 27\right).\]

\[N_{4,3}(h)=h^{3} \left(h^{3} + 9 h^{2} + 18 h + 9\right).\]

## Dimension 5

\[D_{5}(h)=25 h^{8} + 200 h^{7} + 800 h^{6} + 2200 h^{5} + 4520 h^{4} + 6720 h^{3} + 6840 h^{2} + 4320 h + 1296.\]

\[N_{5,0}(h)=5 h^{8} + 20 h^{7} + 20 h^{5} + 536 h^{4} + 1824 h^{3} + 3168 h^{2} + 3024 h + 1296.\]

\[N_{5,1}(h)=h \left(5 h^{7} + 30 h^{6} + 150 h^{5} + 680 h^{4} + 1896 h^{3} + 3168 h^{2} + 3024 h + 1296\right).\]

\[N_{5,2}(h)=h^{2} \left(5 h^{6} + 40 h^{5} + 230 h^{4} + 780 h^{3} + 1476 h^{2} + 1512 h + 648\right).\]

\[N_{5,3}(h)=h^{3} \left(5 h^{5} + 50 h^{4} + 240 h^{3} + 540 h^{2} + 576 h + 216\right).\]

\[N_{5,4}(h)=h^{4} \left(5 h^{4} + 60 h^{3} + 180 h^{2} + 180 h + 36\right).\]

## Dimension 6

\[D_{6}(h)=\left(2 h^{2} + 4 h + 3\right) \left(h^{4} + 4 h^{3} + 10 h^{2} + 24 h + 36\right) \left(3 h^{4} + 12 h^{3} + 22 h^{2} + 24 h + 12\right).\]

\[N_{6,0}(h)=h^{10} + 5 h^{9} - 5 h^{8} - 50 h^{7} + 26 h^{6} + 664 h^{5} + 2280 h^{4} + 4440 h^{3} + 5400 h^{2} + 3888 h + 1296.\]

\[N_{6,1}(h)=h \left(h^{9} + 7 h^{8} + 36 h^{7} + 214 h^{6} + 904 h^{5} + 2472 h^{4} + 4512 h^{3} + 5400 h^{2} + 3888 h + 1296\right).\]

\[N_{6,2}(h)=h^{2} \left(h^{8} + 9 h^{7} + 63 h^{6} + 316 h^{5} + 996 h^{4} + 2016 h^{3} + 2592 h^{2} + 1944 h + 648\right).\]

\[N_{6,3}(h)=h^{3} \left(h^{7} + 11 h^{6} + 76 h^{5} + 300 h^{4} + 696 h^{3} + 960 h^{2} + 720 h + 216\right).\]

\[N_{6,4}(h)=h^{4} \left(h^{6} + 13 h^{5} + 75 h^{4} + 210 h^{3} + 306 h^{2} + 204 h + 36\right).\]

\[N_{6,5}(h)=h^{5} \left(h^{5} + 15 h^{4} + 60 h^{3} + 90 h^{2} + 36 h - 12\right).\]

For every integer \(2\le n\le5\), the denominators and numerators have nonnegative coefficients, with strictly positive values for \(h>0\). For six states the numerator indexed five alone can change sign. The diagonal-numerator interval argument is in `RESULT.md`.
